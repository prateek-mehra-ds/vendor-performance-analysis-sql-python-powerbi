# Vendor Performance Analysis - Retails Inventory & Sales

_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions
using SQL, Python, and Power Bl._

## Table of Contents
- [Overview](#overview)
- [Business Problem](#business_problem)
- [Dataset](#dataset)
- [Tools & Technologies](#tools_&_technologies)
- [Project Structure](#project_structure)
- [Data Cleaning & Preparation](#data_cleaning_&_preparation)
- [Exploratory Data Analysis (EDA)](#exploratory_data_analysis__eda_)
- [Research Questions - Key Findings](#research_questions_-_key_findings)
- [Dashboard](#dashboard)
- [How to Run this project](#how_to_run_this_project)
- [Final Recommendation](#final_recommendation)
- [Author Contact](#author_contact)

# Overview

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for
purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL,
Python for analysis and hypothesis testing, and Power BI for visualization.

# Business Problem

Effective inventory and sales management are critical in the retail sector. This project aims to:
- Identify underperforming brands needing pricing or promotional adjustments
- Determine vendor contributions to sales and profits
- Analyze the cost—benefit of bulk purchasing
- Investigate inventory turnover inefficiencies
- Statistically validate differences in vendor profitability

# Dataset

- dataset link is in '/data/' folder consists of zip file in which (sales, inventory, vendors) csv files are compressed.
- Sumary table created from ingested data and used for analysis

# Tools & Technologies
- SQL (Common Table Expressions, Joins, Filtering)
- Python (Pandas, Matplotlib, Seaborn, SciPy)
- Power BI (Interactive Visualizations)
- GitHub

## Project Structure

vendor—performance—analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
├── vendor_performance_report.pdf
│
├── notebooks/                   Jupyter notebooks
│   ├── exploratory_data_analysis.ipynb
│   └── vendor_performance_analysis.ipynb
│
├── scripts/                    Python scripts for ingestion and processing
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── outputs/                    csv file for further analysis
│   └── vendor_sales_summary.csv
│
├── dashboard/                  Power BI dashboard file
│   └── vendor_performance.pbix

````
vendor-performance-analysis/
│
├── 📄 README.md
├── 🛑 .gitignore
├── 📦 requirements.txt
├── 📑 vendor_performance_report.pdf
│
├── 📓 notebooks/       # Jupyter notebooks
│ ├── 📘 exploratory_data_analysis.ipynb
│ └── 📗 vendor_performance_analysis.ipynb
│
├── 🐍 scripts/         # Python scripts for ingestion and processing
│ ├── 📜 ingestion_db.py
│ └── 📜 get_vendor_summary.py
│
├── 📊 outputs/         # CSV file for further analysis
│ └── 📄 vendor_sales_summary.csv
│
├── 📈 dashboard/       # Power BI dashboard file
│ └── 📊 vendor_performance.pbix
````


# Data Cleaning & Preparation

-  Removed transactions with:
 - Gross Profit ≤ 0
 - Profit Margin ≤ 0
 - Sales Quantity = Ø
- Created summary tables with vendor-level metrics
- Converted data types, handled outliers, merged lookup tables

---
# Exploratory Data Analysis (EDA)

**Negative or Zero Values Detected:**
 - Gross Profit: Min -52,002.78 (loss-making sales)
 - Profit Margin: Min -∞ (sales at zero or below cost)
 - Unsold Inventory: Indicating stow—moving stock

**"Outliers Identified:"**
 - High Freight Costs (up to 257K)
 - Large Purchase/Actuat Prices

**"Correlation Analysis:"**
 - Weak between Purchase Price & Profit
 - Strong between Purchase Qty & Sates Qty (O.999)
 - Negative between Profit Margin & Sales Price (-0.179)
---
