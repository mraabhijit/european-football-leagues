# European Football Leagues


### Strategy

source --> gcs (data lake) (mage)
gcs --> bq (data warehouse) (mage)
bq --> bq (transformation) (dbt/spark/others...)
bq --> dashboard (powerbi/looker)


### Prerequisities

Install docker, docker-compose, terraform, git, any IDE, GCP account.

### Current Status

Captured matchday data for top 5 football leagues (2023) in Europe and transformed into dataframes, teams data.

Added connected pipelines from ingestion to data warehousing. 

Next step is to find a way to trigger manual activation of first pipeline without having to go to mage ui.
Create partitioned table on leagues, create final league tables on dbt. 
Create dashboard on Looker/Power BI.
