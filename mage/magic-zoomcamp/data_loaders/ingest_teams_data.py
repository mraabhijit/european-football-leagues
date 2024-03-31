import io
import os
import pandas as pd
import requests
import json
from dotenv import main

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

print("Started pipeline: ingest_data_to_data_lake_teams ...")

# Get footall-org-data key
main.load_dotenv()

headers = { 
    'X-Auth-Token': os.getenv('X_AUTH_TOKEN')
}


teams = {"PL": "Premier League", 
        "BL1": "Bundesliga",
        "FL1": "Ligue 1",
        "PD": "La Liga",
        "SA": "Serie A"}

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    print("Started running ingest_teams_data.py ...")

    base_uri = "https://api.football-data.org/v4/competitions/"

    team_dict = {}

    for key, value in teams.items():
        uri = base_uri + key + '/teams'

        print(f"Getting data for {value} teams")
        try: 
            response = requests.get(uri, headers=headers)

            team_dict[value] = response.json()['teams']
        except FileNotFoundError:
            print("Data not available at {uri}")

    print("...succesfully ran ingest_teams_data.py")
    
    return team_dict

    
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['Premier League'] is not None, f'Key "Premier League" not found.'

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['Bundesliga'] is not None, f'Key "Bundesliga" not found.'

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['Ligue 1'] is not None, f'Key "Ligue 1" not found.'

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['La Liga'] is not None, f'Key "La Liga" not found.'

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['Serie A'] is not None, f'Key "Serie A" not found.'
