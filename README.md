# SAP Python ETL Pipeline: SAP to PostgreSQL Data Warehouse

## Overview

This project demonstrates a robust ETL (Extract, Transform, Load) pipeline built using Python. The pipeline connects to an SAP system, extracts data from various models and tables, performs necessary transformations, and loads the processed data into a PostgreSQL Data Warehouse. The entire workflow is orchestrated using Apache Airflow, enabling efficient scheduling, monitoring, and management of the ETL processes.

## Features

- **SAP Integration:** Extract data from SAP tables using the SAP RFC SDK and Python's `pyrfc` library.
- **Data Transformation:** Cleanse, transform, and prepare the data for loading into the Data Warehouse.
- **PostgreSQL Integration:** Load the transformed data into a PostgreSQL Data Warehouse.
- **Complex Queries:** Create complex views in PostgreSQL to enable advanced data analysis.
- **Workflow Management:** Use Apache Airflow to manage and automate the ETL pipeline.

## Prerequisites

Before running the ETL pipeline, ensure that the following software is installed on your system:

- **Python 3.8+**
- **PostgreSQL**
- **Apache Airflow**
- **SAP RFC SDK**
- **Git**

## Installation

### Step 1: Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/MaroofAshraf/sap-PythonEtl-pipeline-SAPtoPostgresDW.git
cd sap-PythonEtl-pipeline-SAPtoPostgresDW

### Step 2: Set Up a Virtual Environment
Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Step 3: Install Dependencies
Install the necessary Python packages:

pip install -r requirements.txt

### Step 4: Configure SAP Connection
Edit the config/sap_config.json file with your SAP credentials:

{
  "user": "your_sap_user",
  "passwd": "your_sap_password",
  "ashost": "sap_server_host",
  "sysnr": "system_number",
  "client": "client_number",
  "lang": "EN"
}

### Step 5: Set Up PostgreSQL
Ensure that PostgreSQL is installed and running. Create a new database for the project:

CREATE DATABASE sap_data_dw;

### Step 6: Initialize Airflow
Initialize the Airflow database and create an admin user:

airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com

Start the Airflow web server and scheduler:

airflow webserver --port 8080
airflow scheduler
Access the Airflow web interface at http://localhost:8080.

Running the ETL Pipeline
Trigger the DAG: Trigger the Airflow DAG manually from the Airflow web interface or let it run on the defined schedule.

Monitor the Pipeline: Use the Airflow interface to monitor the execution of each task in the DAG.

Query the Data: Once the data is loaded into PostgreSQL, you can run complex queries against it. For example:

SELECT * FROM material_summary;

## Testing
Unit and integration tests are provided to validate each component of the ETL pipeline. To run the tests:

### Using pytest
pytest tests/

### Using unittest
python -m unittest discover tests/

For any questions or issues, please feel free to open an issue in this repository or contact me directly.