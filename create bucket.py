# ***********************************************************************************************************
"""" ******************* For creating bucket using bigquery ******************* """
# ***********************************************************************************************************

#pip install google-cloud-storage

from google.cloud import storage

# Replace 'your-project-id' and 'your-bucket-name' with your actual Google Cloud project ID and desired bucket name
project_id = 'your-project-id'
bucket_name = 'your-bucket-name'

# Create a Cloud Storage client
storage_client = storage.Client(project=project_id)

# Create a new bucket
bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")
