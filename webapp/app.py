from flask import Flask, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)

def fetch_data():
    conn = psycopg2.connect(
        host="db",
        database="telecomdb",
        user="postgres",
        password="postgres"
    )
    query = "SELECT severity, COUNT(*) FROM telecom_alarms GROUP BY severity;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

@app.route("/")
def dashboard():
    df = fetch_data()
    labels = df['severity'].tolist()
    values = df['count'].tolist()
    return render_template("dashboard.html", labels=labels, values=values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

