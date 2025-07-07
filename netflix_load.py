import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

# Load raw data (replace with your actual file)
df = pd.read_csv("/opt/airflow/data/raw/netflix_watch_logs_20250707_125503.csv")

# Drop rows with missing critical fields
df = df.dropna(subset=["user_id", "content_id", "genre", "device", "country", "watch_start", "watch_duration_min"])

# Convert watch_start to datetime
df["watch_start"] = pd.to_datetime(df["watch_start"], errors="coerce")

# Drop rows with invalid datetime
df = df.dropna(subset=["watch_start"])

# Feature engineering
df["watch_year"] = df["watch_start"].dt.year
df["watch_month"] = df["watch_start"].dt.month
df["watch_day"] = df["watch_start"].dt.day
df["watch_weekday"] = df["watch_start"].dt.day_name()
df["hour_of_day"] = df["watch_start"].dt.hour

# Flag binge watchers (arbitrary threshold: >150 mins)
df["is_binge"] = df["watch_duration_min"] > 150

# Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Add a load timestamp
df["load_timestamp"] = datetime.now()

# Connect to PostgreSQL
engine = create_engine("postgresql://airflow:airflow@postgres:5432/analytics")

# Create schema if it doesn't exist
with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS data_etl"))

# Append data
df.to_sql("netflix_watch_logs", engine, schema="data_etl", if_exists="append", index=False)

print("✅ ETL completed: data appended to data_etl.netflix_watch_logs.")
