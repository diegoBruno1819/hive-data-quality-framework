# Hive Data Quality Framework

![Python](https://img.shields.io/badge/python-3.10-blue)
![Hive](https://img.shields.io/badge/apache-hive-yellow)
![Data Engineering](https://img.shields.io/badge/data-engineering-green)

Lightweight Python framework to perform automated data quality checks on Apache Hive tables.

## Overview

This project simulates a common Data Engineering scenario where data quality validations must be executed before data is consumed by downstream pipelines.

The framework performs automated checks on Hive tables using Python and SQL.

## Features

- Duplicate detection
- NULL value validation
- Row count monitoring
- Modular validation scripts
- Automated report generation

## Architecture
Data Source (Hive Table)
│
▼
Python Data Quality Framework
│
├── Duplicate Check
├── NULL Check
└── Row Count Check
│
▼
Data Quality Report


## Project Structure
hive-data-quality-framework

checks/
check_duplicates.py
check_nulls.py
check_rowcount.py

reports/
report_generator.py

sql/
duplicates_query.sql
nulls_query.sql

config.yaml
run_checks.py


## Technologies

- Python
- SQL
- Apache Hive
- Linux

## Example Output
DATA QUALITY REPORT

duplicates_found: 0
null_values: 12
row_count: 1045821


## Use Case

In many data platforms, validating data before it enters analytics layers is critical.

This project demonstrates a simple but extensible framework that can be used to automate common data quality checks in ETL pipelines.

## Future Improvements

- Integration with Airflow
- Alerting via email or Slack
- Historical data quality metrics
- AWS integration
