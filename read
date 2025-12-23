# Databricks-DLT-End-To-End-Pipeline

# End-to-End Data Engineering Project Using Databricks Delta Live Tables (DLT)

## Overview

This project showcases a complete end-to-end **data engineering pipeline** built using **Databricks Delta Live Tables (DLT)**.  
It follows a production-grade **Bronze → Silver → Gold** Lakehouse architecture and demonstrates how to ingest, clean, transform, and model data for real-time analytics.

The goal is to build an automated and scalable ETL pipeline that supports:
- Streaming ingestion
- Incremental transformations
- SCD Type 1 and Type 2 logic
- Auto CDC processing
- Fact and Dimension modeling

The output data is optimized for downstream consumption by **Data Scientists, BI dashboards, and analytical applications**.

## Key Objectives
- Ingest raw data into Bronze using Auto Loader.
- Build Silver streaming views with transformations.
- Apply SCD1 logic for Silver streaming tables.
- Build Gold layer with dimensions (SCD2) and a Fact table (SCD1).
- Use DLT Auto CDC for incremental modeling.
- Create clean, analytics-ready tables.

## Dataset
The project uses four key datasets stored in cloud/Object Storage:
- Customers  
- Products  
- Sales  
- Stores  

Each dataset simulates events generated from an e-commerce environment and is processed using DLT streaming tables.

Dataset relationships include:
- Sales linked to customers, products, and stores.
- Customers linked through domain/email fields.
- Stores linked to sales transactions.

The datasets are intentionally simple but structured to demonstrate a full Lakehouse pipeline.

---

## Project Modules

The project is divided into structured Python modules inside the `transformations/` directory.  
Each module is executed as part of the Delta Live Tables pipeline.

### Module 1: Bronze Layer (Ingestion)
- Ingest raw CSV data using **cloudFiles** (Auto Loader).
- Build **streaming ingestion tables**:
  - `customers_bronze`
  - `products_bronze`
  - `sales_bronze`
  - `stores_bronze`
- Auto Loader handles schema inference and incremental loading.
- Data stored in Delta format for reliability.

### Module 2: Silver Layer (Transformations & Cleaning)
- Build **streaming views** for each Bronze table.
- Transformations include:
  - Standardizing columns  
  - Extracting email domains  
  - Creating derived metrics  
  - Data cleaning using PySpark  
  - Adding `processDate` timestamps  
- Create **Silver streaming tables using SCD Type 1**:
  - `customers_silver`
  - `products_silver`
  - `sales_silver`
  - `stores_silver`
- Uses `dlt.create_auto_cdc_flow()` to automatically upsert changes.

### Module 3: Gold Layer (Dimensional Modeling)
- Gold layer consumes **Silver Views**, not Silver tables, ensuring clean lineage.
- Create **Gold Views** for analytics:
  - `customers_gold_view`
  - `products_gold_view`
  - `sales_gold_view`
  - `stores_gold_view`
- Build dimension tables with **SCD Type 2**:
  - `dim_customers`
  - `dim_products`
  - `dim_stores`
- Build fact table with **SCD Type 1**:
  - `fact_sales`

The Gold layer represents a fully modeled star-schema layout.

### Module 4: Auto CDC & Incremental Processing
- Automatically identifies inserts/updates/deletes.
- Handles late-arriving data gracefully.
- Maintains history for dimensions (SCD2) and performs upserts for facts (SCD1).

### Module 5: Serving Layer
- Final Gold Tables are ready for:
  - BI tools (Tableau, Power BI)
  - Machine learning feature generation
  - Ad-hoc analytics
  - Dashboarding via Databricks SQL

All Gold-layer tables are **optimized Delta tables** for fast reads.

---

## Technologies Used
- **Databricks**
- **Delta Live Tables (DLT)**
- **Apache Spark (PySpark)**
- **Delta Lake**
- **Auto Loader (cloudFiles)**
- **Streaming ETL**
- **SCD1 & SCD2**
- **CDC Processing**

---

## Project Structure

DLT_ENDTOEND1/
│
├── transformations/
│ ├── bronze/
│ │ └── ingestion.py
│ │
│ ├── silver/
│ │ ├── customers_silver.py
│ │ ├── products_silver.py
│ │ ├── sales_silver.py
│ │ └── store_silver.py
│ │
│ ├── gold/
│ │ ├── dim_customers.py
│ │ ├── dim_products.py
│ │ ├── dim_stores.py
│ │ └── fact_sales.py
│
├── utilities/
│ └── utils.py
│
└── README.md
