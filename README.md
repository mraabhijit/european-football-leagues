# European Football Leagues


### Strategy

source --> gcs (data lake) (mage)
gcs --> bq (data warehouse) (spark/dbt)
bq --> dashboard (powerbi/looker)


### Prerequisities

Install docker, docker-compose, terraform, git, any IDE

### Current Status

Captured matchday data for top 5 football leagues (2023) in Europe and transformed into dataframe.
Next step is to get data regarding teams/clubs in the leagues and their key members like Owner, Manager, Established date
