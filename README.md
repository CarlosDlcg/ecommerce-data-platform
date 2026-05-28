# Ecommerce Data Platform

Modern Data Engineering project that simulates a production-ready data platform for an e-commerce company using:

- PySpark
- dbt
- Apache Airflow
- PostgreSQL
- Docker

The pipeline ingests data from multiple sources, processes it through scalable Spark transformations, and prepares analytics-ready datasets using modern data engineering practices.

---

# Project Goals

This project demonstrates:

- Multi-source data ingestion
- Distributed data processing with Spark
- Layered data architecture
- Incremental and scalable transformations
- Historical tracking with SCD Type 2
- Workflow orchestration with Airflow
- Data quality validation and monitoring

---

# Architecture

```text
Sources
│
├── PostgreSQL
├── REST API
└── CSV Files
        ↓
RAW Layer
(data/raw)
        ↓
PySpark Transformations
        ↓
STAGING Layer
(data/staging)
        ↓
dbt Models & SCD2
        ↓
Analytics Layer
        ↓
Airflow Orchestration
```

---

# Tech Stack

| Tool | Purpose |
|---|---|
| Python | Pipeline development |
| PySpark | Distributed processing |
| PostgreSQL | Source & warehouse storage |
| dbt | Transformations & SCD2 |
| Apache Airflow | Workflow orchestration |
| Docker | Local infrastructure |
| Pandas | Lightweight ingestion |
| SQLAlchemy | Database connectivity |

---

# Current Features

## Data Ingestion
- PostgreSQL extraction
- REST API extraction
- CSV ingestion
- Timestamped RAW persistence

## Spark Processing
- Schema enforcement
- Deduplication
- Null handling
- Technical metadata cleanup
- Parquet staging layer

## Engineering Practices
- Modular architecture
- Centralized logging
- Retry handling
- Environment-based configuration

---

# Project Structure

```text
ecommerce-data-platform/
│
├── airflow/
├── configs/
├── data/
│   ├── raw/
│   └── staging/
├── logs/
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── utils/
│   └── config/
├── tests/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Setup

## Clone repository

```bash
git clone <repo-url>
cd ecommerce-data-platform
```

## Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

```bash
cp .env.example .env
```

## Start PostgreSQL

```bash
docker compose up -d
```

---

# Running the Pipeline

## Run ingestion layer

```bash
python -m src.extract.run_extractors
```

## Run Spark transformations

```bash
python -m src.transform.run_transformations
```

---

# Next Steps

- dbt dimensional modeling
- SCD Type 2 snapshots
- Fact tables
- Airflow DAG orchestration
- Data quality reports
- Monitoring and alerting

---

# Author

Carlos De los Cobos