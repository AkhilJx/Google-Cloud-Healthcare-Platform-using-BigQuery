# ***********************************************************************************************************
"""" ******************* For creating table using bigquery ******************* """
# ***********************************************************************************************************

# pip install google-cloud-bigquery

import os
from google.cloud import bigquery

# replace ******-******-******-************.json with ur credentials
credential_path = "C:/Users/AKHIL JX/Downloads/******-******-******-************.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Replace 'YOUR_PROJECT_ID' and 'YOUR_DATASET_ID' with your project and dataset IDs
project_id = 'YOUR_PROJECT_ID'
dataset_id = 'YOUR_DATASET_ID'
table_id = 'new_table'

# Create a BigQuery client
client = bigquery.Client(project=project_id)

# Define the table reference
table_ref = client.dataset(dataset_id).table(table_id)

# Define the schema of the table
schema = [
    bigquery.SchemaField("column1", "STRING"),
    bigquery.SchemaField("column2", "INTEGER"),
    # Add more columns as needed
]

# Create the table
table = bigquery.Table(table_ref, schema=schema)
table = client.create_table(table)

print(f'Table {table.table_id} created in dataset {dataset_id}')
