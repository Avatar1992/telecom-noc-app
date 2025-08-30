# 📡 Telecom NOC ETL Dashboard

This project demonstrates a **real-time ETL pipeline** for Telecom **OSS alarms**.  
It extracts raw alarms from OSS (CSV), loads them into **PostgreSQL**, and visualizes them in a **Flask + Chart.js web dashboard**.  

## 🚀 Features

- ETL pipeline (Extract → Transform → Load)
- PostgreSQL database for alarm storage
- Flask web dashboard
- Bootstrap + Chart.js visualization
- Docker & Docker Compose orchestration

## 🏗️ Project Architecture

OSS CSV → ETL (Python) → PostgreSQL → Flask Web App → Dashboard (HTML + Charts)


## 📂 Project Structure

telecom-noc-app/
│── etl/ (ETL Service)
│── web/ (Flask Dashboard)
│── docker-compose.yml
│── README.md


## ⚙️ Prerequisites
- Docker & Docker Compose installed

## ▶️ Run the Project

docker-compose up --build -d

Access:

Flask Dashboard → http://localhost:5000
PostgreSQL DB → localhost:5432

Stop services:
docker-compose down

<img width="1920" height="1075" alt="Screenshot from 2025-08-30 17-59-21" src="https://github.com/user-attachments/assets/b0fa2b13-26d3-44cc-b0a6-543f3fb6d8f3" />


