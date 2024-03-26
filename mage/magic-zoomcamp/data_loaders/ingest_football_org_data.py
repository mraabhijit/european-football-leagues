import io
import pandas as pd
import requests
import json
import time

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# Define function to get key and read key for football-data.org
def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys(".secret/football-data.json")
headers = { 
    'X-Auth-Token': keys["X-Auth-Token"] 
}


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    base_url = "https://api.football-data.org/"
    comp = 'v4/competitions/'
    matchday = "//matches?matchday="

    matchdays = {"PL": ["Premier League", 38], 
                "BL1": ["Bundesliga", 34],
                "FL1": ["Ligue 1", 34],
                "PD": ["La Liga", 38],
                "SA": ["Serie A", 38]}

    match_list = {}
    count = 1
    for key, value in matchdays.items():
        print(f"Getting data for {value[0]}")
        match_list[value[0]] = []
        for i in range(value[1]):
            uri = base_url + comp + key + matchday + f"{i+1}"
            # print(f"Getting data from {uri}")
            if count > 10 and count%10 == 1:
                time.sleep(60)
            try: 
                response = requests.get(uri, headers=headers)

                data = response.json()
                
                match_list[value[0]].append(data)

            except FileNotFoundError:
                print("matchday data not available")
            count += 1
        print(f"Successfully got data for {value[0]}")

    return match_list

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
