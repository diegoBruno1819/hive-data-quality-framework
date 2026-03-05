# Hive Data Quality Framework

A lightweight Python framework designed to perform automated data quality checks on Apache Hive tables.

## Features

- Duplicate detection
- NULL value validation
- Row count monitoring
- Automated reporting

## Technologies

- Python
- Apache Hive
- SQL
- Linux

## Project Structure

hive-data-quality-framework

checks → data validation scripts  
reports → report generation  
config.yaml → configuration file  
run_checks.py → main execution script

## Example Output

DATA QUALITY REPORT

duplicates_found: 0  
null_values: 5  
row_count: 1023481

## Use Case

This project simulates a common Data Engineering task: validating data before it is used in downstream ETL pipelines.
