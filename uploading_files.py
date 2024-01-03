# ***********************************************************************************************************
"""" ******************* For uploading the data for table4 creation ******************* """
# ***********************************************************************************************************

import json
import time
import os
from google.cloud import bigquery

# ***********************************************************************************************************

# replace ******-******-******-************.json with ur credentials
credential_path = "C:/Users/AKHIL JX/Downloads/******-******-******-************.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# ***********************************************************************************************************

json_data = json.load(open("C:/Users/AKHIL JX/Downloads/test_data.json"))
data_file_path = "json_upload.json"
with open(data_file_path,"w") as _f:
    _f.write("\n".join(json.dumps(row) for row in json_data))

# ***********************************************************************************************************

client = bigquery.Client()

# ***********************************************************************************************************

# replace ******-******-******.dataset1.table4 with ur credentials
table_id = "`******-******-******.dataset1.table4"

# ***********************************************************************************************************

job_config = bigquery.LoadJobConfig(
    autodetect = True,
    source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    write_disposition = "WRITE_APPEND"
)

# ***********************************************************************************************************

with open(data_file_path,"rb") as source_file:
    job = client.load_table_from_file(source_file,table_id,job_config = job_config)

while job.state != "DONE":
    job.reload()
    time.sleep(2)
print(job.result())

# ***********************************************************************************************************