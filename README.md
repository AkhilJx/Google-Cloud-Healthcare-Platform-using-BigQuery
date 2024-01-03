# Google-Cloud-Healthcare-Platform using BigQuery
various google cloud operations to facilitate Google Cloud Healthcare API using BigQuery

This repository/program was a part of investigating FHIR / Dicom formats of healthcare data. 

Google Healthcare API: A secure, compliant, fully managed service for ingesting, transforming and storing healthcare data in FHIR, HL7v2, and DICOM formats, and unstructured text.

COMMON USES: Store, manage, and query FHIR data

Google BigQuery: BigQuery is a fully managed enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence.

Implementation:

1. First Go to the Google Cloud Console.
2. Open the Google Cloud Console.
3. Select or Create a Project:If you haven't created a project, you need to create one. If you already have a project, ensure it's selected in the top bar of the console.
4. Navigate to the IAM & Admin Section: In the left sidebar, click on "IAM & Admin" and then select "Service accounts."
5. Create a Service Account:Click the "Create Service Account" button.
6. Give your service account a name.
7. Optionally, set a description for the service account.
8. Click "Create."
9.Grant Roles to the Service Account:In the "Service account permissions" step, grant the necessary roles to the service account. At a minimum, you will likely need the "BigQuery Admin" or BigQuery Data Editor role. You can add more roles based on your project's requirements.
10.Create a new key: Click on the "Add Key" button.
11.Choose the JSON key type.
12.Download the Key File:

A JSON file containing your service account key will be downloaded to your computer. This file is the Service Account Key, and you will use its path in your code to authenticate with Google Cloud services.

Now you have the service account key JSON file. This file contains the credentials needed to authenticate your application with Google Cloud services. Keep it secure, and do not expose it publicly.
Remember that service account keys grant significant permissions, so use them with care. Avoid hardcoding the key directly in your code and consider using environment variables or a secure configuration management solution to handle the key in a more secure way.

When using the Service Account Key in your code, set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the downloaded JSON key file. This allows the Google Cloud client libraries to find and use the credentials automatically.

Google Buckets:

In Google BigQuery, a "bucket" typically refers to a Cloud Storage bucket, not directly within BigQuery itself. Cloud Storage is a separate service in Google Cloud Platform that provides object storage. You might use a Cloud Storage bucket to store and manage data files that you want to analyze using BigQuery.

Here's a brief explanation of the use of a Cloud Storage bucket in conjunction with BigQuery:

1. Storage for Data: You can store large datasets in Cloud Storage buckets. These datasets can then be imported into BigQuery for analysis.

2. Data Loading: When you want to load data into BigQuery, you often do so by referencing files stored in a Cloud Storage bucket. BigQuery can read directly from Cloud Storage, allowing for efficient data loading.

3. Exporting Results: After running queries in BigQuery, you can export the results to a Cloud Storage bucket for further processing or storage.


To create a Cloud Storage bucket in Python, you would typically use the google-cloud-storage library, which is part of the Google Cloud Client Libraries. 


There are many operations of Bigquery that are carried out in this project which is specified as individual projects in the repository.
