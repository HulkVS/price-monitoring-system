import streamlit as st
import pandas as pd
import boto3

st.set_page_config(page_title="Price Monitor", layout="wide")
st.title("💰 Real-Time Competitor Price Dashboard")

# Athena Config
athena = boto3.client('athena', region_name='us-east-1')

S3_OUTPUT = 's3://surya-price-monitoring/athena-results/'
DATABASE = 'default'
TABLE = 'price_logs'

def run_query(query):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': DATABASE},
        ResultConfiguration={'OutputLocation': S3_OUTPUT}
    )
    exec_id = response['QueryExecutionId']

    while True:
        result = athena.get_query_execution(QueryExecutionId=exec_id)
        state = result['QueryExecution']['Status']['State']
        if state in ['SUCCEEDED', 'FAILED']:
            break

    if state == 'SUCCEEDED':
        results = athena.get_query_results(QueryExecutionId=exec_id)
        rows = results['ResultSet']['Rows'][1:]
        columns = [col['VarCharValue'] for col in results['ResultSet']['Rows'][0]['Data']]
        data = [[cell.get('VarCharValue', '') for cell in row['Data']] for row in rows]
        return pd.DataFrame(data, columns=columns)
    else:
        st.error("Query failed.")
        return pd.DataFrame()

# Get data
query = f"SELECT * FROM {TABLE} ORDER BY timestamp DESC LIMIT 50"
df = run_query(query)

# Show data
if not df.empty:
    df['target_price'] = df['target_price'].astype(float)
    df['current_price'] = df['current_price'].astype(float)

    st.dataframe(df)

    st.subheader("📉 Price Drops")
    drops = df[df['current_price'] < df['target_price']]
    st.table(drops)

    st.subheader("📈 Price Trend")
    chart_df = df.groupby('product_name').mean(numeric_only=True)
    st.line_chart(chart_df[['current_price']])
else:
    st.warning("No data found.")
