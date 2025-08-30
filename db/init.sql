CREATE TABLE IF NOT EXISTS telecom_alarms (
    id SERIAL PRIMARY KEY,
    site_id INT,
    site_name VARCHAR(100),
    alarm_code VARCHAR(20),
    severity VARCHAR(20),
    status VARCHAR(20),
    timestamp TIMESTAMP
);

