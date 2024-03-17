# Building a Cricket Team Ranking pipeline using Google Cloud Services

## Introduction:
Our project focuses on leveraging Python's capabilities to interface with APIs, specifically the Cricbuzz API, to retrieve comprehensive cricket statistics efficiently. This README provides an overview of the various stages involved in our data retrieval and processing pipeline.

### Architecture
![Architecture](https://github.com/VachanPatil30/Cricket-Team-Ranking-pipeline-using-GCP/assets/79377852/aa3e61bd-a4c9-409b-a688-f004fe1421f7)

### 1. Data Retrieval from Cricbuzz API:
Utilizing Python, we interact with the Cricbuzz API to fetch cricket statistics, including One Day International (ODI) team rankings. Python's versatility enables efficient data retrieval, facilitating subsequent processing stages.

### 2. Storing Data in Google Cloud Storage (GCS):
After obtaining the data, our next objective is to securely preserve it in the cloud. We employ Google Cloud Storage (GCS) to store the data in CSV format, ensuring accessibility and scalability for future processing tasks.

### 3. Creating a Cloud Function Trigger:
To automate our pipeline, we set up a Cloud Function that triggers upon file upload to the GCS bucket. This function serves as the initiator for subsequent data processing steps, streamlining the workflow.

### 4. Execution of the Cloud Function:
Within the Cloud Function, meticulous code is crafted to precisely trigger a Dataflow job. We handle triggers and pass requisite parameters to seamlessly initiate the Dataflow job, ensuring smooth data processing.

### 5. Dataflow Job for BigQuery:
The core component of our pipeline is the Dataflow job, orchestrated by the Cloud Function trigger. This job facilitates the transfer of data from the CSV file in GCS to BigQuery. We configure job settings meticulously to ensure optimal performance and accurate data ingestion into BigQuery.

### 6. Looker Dashboard Creation:
Lastly, we explore BigQuery's potential as a data source for Looker Studio. By configuring Looker to connect with BigQuery, we create visually compelling dashboards. These dashboards serve as the visualization hub, enabling insightful analysis based on the cricket statistics data loaded from our pipeline, including ODI team rankings.
