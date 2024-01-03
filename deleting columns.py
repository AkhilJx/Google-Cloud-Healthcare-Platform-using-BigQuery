import time
import os
from google.cloud import bigquery

# ***********************************************************************************************************

credential_path = "C:/Users/AKHIL JX/Downloads/prefab-imagery-373210-9afee1a6724f.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# ***********************************************************************************************************

# Construct a BigQuery client object.
client = bigquery.Client()

# ***********************************************************************************************************

dataset_ref = bigquery.DatasetReference(client.project,"dataset1")
table_ref = bigquery.TableReference(dataset_ref,"table4")
bigquery_table = client.get_table(table_ref)

# ***********************************************************************************************************

# get a snapshot of the table schema
original_schema = bigquery_table.schema

# Add columns
new_schema = original_schema[:]  # Creates a copy of the schema.
new_schema.append(bigquery.SchemaField("saved2", "BOOLEAN", mode="NULLABLE"))
new_schema.append(bigquery.SchemaField("permalink2", "STRING", mode="NULLABLE"))

# assign the updated schema to the bigquery_table
bigquery_table.schema = new_schema

# make an API request to add columns
client.update_table(bigquery_table, ['schema'])

# delete columns
query_job = client.query("""
    ALTER TABLE dataset1.table4
    DROP COLUMN IF EXISTS saved2,
    DROP COLUMN IF EXISTS permalink2;
                         """)

while query_job.state != 'DONE':
    print('Waiting for job to finish...')
    time.sleep(3)
    query_job.reload()
print(query_job.result())
