# European Football Leagues


## Strategy

Insert DAG Image here

## Prerequisities

    - docker
    - docker-compose
    - terraform
    - git
    - any IDE
    - GCP account
    - gcloud (if not working on a GCP VM)

## Steps to Follow:

1. Git clone the repo: 

`git clone https://github.com/mraabhijit/european-football-leagues.git`

2. Create your cloud infrastructure using terraform:

`cd terraform`

Change the following variables as per your setup/keep the existing ones:

- in variables.tf, the default values of
    - variable "project"
    - variable "region"
    - variable "location"
    - variable "bq_dataset_name"
    - variable "gcs_bucket_name"
- in main.tf, 
    - rename "capstone-411615" to default used for "gcs_bucket_name"
    - rename "capstone" to default used for "bq_dataset_name"

Once the names are setup follow the following commands:

```
terraform init
terraform plan
terraform apply
```
**NOTE: terraform plan is to see what changes/resources are getting created. This step is optional but recommended.**

Once the commands are run, go to your GCP Console and check whether the GCS bucket and BQ dataset have been created.

3. Create the .env file by 

```
cd ..
cd mage
cp dev.env .env
```

This will create a new file called .env and will have the variables needed for the project to run set up. Change the credentials under `GCP` and `Football-org` as they are user specific. 

**NOTE: Make sure to use the same credentials as set up in `terraform/variables.tf`.**

4. Create account in (https://www.football-data.org/)
   
Upon creating the account, you will receive an email with the API Key for the account. Save it to the .env file created in previous step under `X_AUTH_TOKEN` without quotes in directory `mage/.env`.

If your API key is `123qwert`, your `.env` file should look like this:

`X_AUTH_TOKEN=123qwert`

**NOTE: If you are using a paid version of the API, your wait times will be lower than the free version, hence in file "mage/magic-zoomcamp/data_loaders/ingest_football_org_data.py" change the lines 48, 49 accordingly. If you are on a free version, the max number of hits per minute is 10 hence the data load takes the bulk of time.**

3. Save your gcp key to 2 folders as: "mage/magic-zoomcamp/.secret/capstone.json" and ".secret/capstone.json"
4. Update the variables.tf and main.tf with your gcp info like variable "project", "region", "location", "bq_dataset_name", "gcs_bucket_name" defaults
5. cd terraform
    terraform plan
    terraform apply 
    **NOTE: If your resources already exist, you will be notified stating the resources already exist.**
6. In a new terminal
    cd mage
    docker pull mageai/mageai:latest to pull the latest docker image of mageai
    docker-compose up to start the server..

    Once the server starts go to localhost:6789 in your browser and go pipelines -> pipeline tagged as first_pipeline(ingest_data_to_data_lake). Go to last block on the pipeline and click on run with all upstream blocks..

    **NOTE TO SELF: Add all possible images and snapshots with steps.**

    Once you do this, your pipelines will keep running one after the other till transformation pipelines in DBT within Mage. After which you shall have the following tables in your bigquery dataset:
    1. stg_matches.sql
    2. stg_matches_info.sql
    3. stg_teams.sql
    4. away_table.sql
    5. home_table.sql
    6. overall_table.sql
    7. matchday_wise_tally.sql

7. Finally you can visualize the dataset by linking to the last 4 tables you created.

8. Once the project is complete. Please remember to close mage first by running docker-compose down in a new terminal on your PC/VM by changing directory to mage. Lastly, close down the GCP resources by a simple 
    terraform destroy.

### Current Status

Captured matchday data for top 5 football leagues (2023) in Europe and transformed into dataframes, teams data.

Added connected pipelines from ingestion to data warehousing. 

Dashboard created. 

Remaining is the README documentation.
