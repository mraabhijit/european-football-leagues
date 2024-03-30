# European Football Leagues


### Strategy

source --> gcs (data lake) (mage)
gcs --> bq (data warehouse) (mage)
bq --> bq (transformation) (mage[dbt])
bq --> dashboard (powerbi/looker)


### Prerequisities

Install docker, docker-compose, terraform, git, any IDE, GCP account.

# Steps to Follow:

1. Git clone the repo:

2. Create account in (https://www.football-data.org/)
   Upon creating the account, you will receive an email with the API Key for the account. Save it in the following format :
   {
    "X-Auth-Token": "..."
    }
    and save as football-data.json in a folder as mage/magic-zoomcamp/.secret/football-data.json

    **NOTE: If you are using a paid version of the API, your wait times will be lower than the free version, hence in file "mage/magic-zoomcamp/data_loaders/ingest_football_org_data.py" change the lines 48, 49 accordingly. If you are on a free version, the max number of hits per minute is 10 hence the data load takes the bulk of time.**

3. Save your gcp key to 2 folders as: "mage/magic-zoomcamp/capstone.json" and ".secret/capstone.json"
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
