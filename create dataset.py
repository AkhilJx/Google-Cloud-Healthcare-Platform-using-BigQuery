# ***********************************************************************************************************
"""" ******************* For creating dataset using bigquery ******************* """
# ***********************************************************************************************************


# pip install google-cloud-bigquery

import os
from google.cloud import bigquery

# replace ******-******-******-************.json with ur credentials
credential_path = "C:/Users/AKHIL JX/Downloads/******-******-******-************.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Replace 'YOUR_PROJECT_ID' with your Google Cloud project ID
project_id = 'YOUR_PROJECT_ID'

# Create a BigQuery client
client = bigquery.Client(project=project_id)

# Define the new dataset ID and dataset reference
dataset_id = 'new_dataset'
dataset_ref = client.dataset(dataset_id)

# Create the dataset
dataset = bigquery.Dataset(dataset_ref)
dataset = client.create_dataset(dataset)

print(f'Dataset {dataset.dataset_id} created in project {project_id}')
