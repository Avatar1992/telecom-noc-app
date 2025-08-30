import psycopg2
import pandas as pd

# DB Connection
conn = psycopg2.connect(
    host="db",
    database="telecomdb",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

# Extract
df = pd.read_csv("/data/oss_alarms.csv")

# Transform
df['severity'] = df['severity'].str.upper()

# Load
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO telecom_alarms (site_id, site_name, alarm_code, severity, status, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row.site_id, row.site_name, row.alarm_code, row.severity, row.status, row.timestamp))

conn.commit()
cur.close()
conn.close()

print("✅ ETL Completed. Data inserted into DB")

