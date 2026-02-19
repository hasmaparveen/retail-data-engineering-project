# Retail Data Engineering Pipeline

## Project Overview
This project simulates an end-to-end retail data engineering pipeline using Python and SQLite.

It follows the Medallion Architecture:
- Bronze Layer → Raw Data Ingestion
- Silver Layer → Data Cleaning & Transformation
- Gold Layer → Business Aggregations
- Warehouse → SQLite Data Storage
- SQL → Analytical Queries

---

## Project Structure

retail-data-engineering-project/
│
├── data/
├── logs/
├── scripts/
│   ├── generate_data.py
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   ├── gold_layer.py
│   ├── load_to_warehouse.py
│
├── sql/
│   └── analytics_queries.sql
│
├── requirements.txt
├── .gitignore
└── README.md

---

## How to Run

### 1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Generate Data
python scripts/generate_data.py

### 4️⃣ Run Pipeline Layers
python scripts/bronze_layer.py
python scripts/silver_layer.py
python scripts/gold_layer.py
python scripts/load_to_warehouse.py

---

## Technologies Used
- Python
- Pandas
- Faker
- SQLite
- SQL
- Medallion Architecture

---

## Learning Outcomes
- Built end-to-end ETL pipeline
- Implemented layered data architecture
- Created local data warehouse
- Practiced production-level project structure
