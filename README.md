# European Football Leagues


### Strategy

source --> gcs (data lake) (mage)
gcs --> bq (data warehouse) (spark/dbt)
bq --> dashboard (powerbi/looker)


### Prerequisities

Install docker, docker-compose, terraform, git, any IDE

### Current Status

Captured matchday data for top 5 football leagues (2023) in Europe and transformed into dataframes, teams data.

Next step is to start working on mage as data orchestrator and push the data to gcs bucket.
