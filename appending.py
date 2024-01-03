import os
from google.cloud import bigquery

# ***********************************************************************************************************

# replace ******-******-******-************.json with ur credentials
credential_path = "C:/Users/AKHIL JX/Downloads/******-******-******-************.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# ***********************************************************************************************************

# Construct a BigQuery client object.
client = bigquery.Client()

# ***********************************************************************************************************

# replace ******-******-******.dataset1 with ur credentials
query = """
SELECT column_name
FROM `******-******-******.dataset1.INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'table4'
"""

# ***********************************************************************************************************

query_job = client.query(query)  # Make an API request.

# ***********************************************************************************************************

print("**************",query_job)
print("@@@@@@@@@@@@",type(query_job))
print("The query data:")

# ***********************************************************************************************************

a=[]
for row in query_job:

    # Row values can be accessed by field name or index.
    # print("name={}, count={}".format(row[2], row["medications"]))
    # print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    a.append(row[0])
    # print(row[0])


# ***********************************************************************************************************

print(a)

# TODO(developer): Set table_id to the ID of table to append to.
table_id = "prefab-imagery-373210.dataset1.table4"

rows_to_insert = [
    {a[0]: "Phred Phlyntstone", a[1]: "qqqqq",a[2]:"K985",a[3]:"wwwwwwww",a[4]:"llllllllll",a[5]:"1975-08-30",a[6]:"q7q8q7q7q78q878"},
    {a[0]: "Wylma Phlyntstone", a[1]: "rtgyh",a[2]:"K597",a[3]:"tttttttt",a[4]:"rrrrrrrrrr",a[5]:"1955-04-27",a[6]:"wer2345r432wwkl"},
]

errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))