# Real-Time Competitor Price Monitoring & Alert System

A full-stack AWS + Python project that tracks competitor product prices in real-time, sends alerts when prices drop below your target, and visualizes trends with an interactive Streamlit dashboard.

---

## Built With

- **AWS Lambda** – Automates competitor price fetching (simulated)
- **Amazon S3** – Stores input product list and price logs
- **Amazon Athena** – Queries price history using SQL
- **Amazon SNS** – Sends email alerts when price drops
- **Streamlit** – Displays live dashboard with price trends
- **Python + Boto3** – Orchestrates all AWS integrations


## Features

- ✅ Simulated real-time price fetching (with random prices)
- ✅ Alerts when current price < target price (via email)
- ✅ Historical price logs saved in S3
- ✅ Queryable with Athena using SQL
- ✅ Dashboard to view price drops and trends

---

## Project Structure

price-monitoring-system/ ├── price_dashboard.py # Streamlit app ├── requirements.txt # Python dependencies ├── .gitignore # Ignored files └── README.md # Project documentation

## How to Run Locally

**1. Clone the Repo**

```bash
git clone https://github.com/HulkVS/price-monitoring-system.git
cd price-monitoring-system

**2. Install Dependencies**
pip install -r requirements.txt

**3. Configure AWS Credentials (once)**
aws configure
Provide your:

Access Key ID
Secret Access Key
Region (e.g., us-east-1)

**4. Run the Dashboard**
streamlit run price_dashboard.py
Visit: http://localhost:8501

****Sample Data Flow****

product_list.csv (S3/input/) ─▶ Lambda (simulates prices)
                                 └──▶ output/price_log_*.csv (S3/output/)
                                            └──▶ Athena (query)
                                                       └──▶ Dashboard + Alerts

👨‍💻 Author
Surya Kiran Reddy Vanukuri
GitHub: @HulkVS



