# ***********************************************************************************************************
"""" ************* Extracting data from a BigQuery table and storing it in a Google Cloud Storage bucket in newline-delimited JSON format. ************* """
# ***********************************************************************************************************

import os
from google.cloud import bigquery

# replace ******-******-******-************.json with ur credentials
credential_path = "C:/Users/AKHIL JX/Downloads/******-******-******-************.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
# POST https://language.googleapis.com/v1/documents:analyzeEntities?key="AIzaSyDhRMXl80-zMp1dL3xVR0x79b6xgMWIHsU"

# API_KEY = "AIzaSyD3C4Zl7xDUHVVTTRim4C7jgm5DaLhyZHE"

# Construct a BigQuery client object.
client = bigquery.Client()

dataset_id = "dataset1"

# replace ******-******-****** with ur credentials
bucket_name = "******-*******-******"

dataset_ref = bigquery.DatasetReference(client.project,dataset_id)
table_ref = dataset_ref.table("resulttable")

job_config = bigquery.job.ExtractJobConfig()
job_config.destination_format = bigquery.DestinationFormat.NEWLINE_DELIMITED_JSON
# job_config.destination_format = bigquery.DestinationFormat.CSV

destination_uri = "gs://{0}/{1}".format(bucket_name,"resulttable.json")
# destination_uri = "gs://qazwsxedcrfvtgb/test_data.json"

extract_job = client.extract_table(
    table_ref,
    destination_uri,
    job_config = job_config,
    location = "us-east1"
)
print(extract_job.result())

