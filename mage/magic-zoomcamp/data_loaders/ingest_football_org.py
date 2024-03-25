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
    # url = ''
    # response = requests.get(url)

    # return pd.read_csv(io.StringIO(response.text), sep=',')

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
            print(f"Getting data from {uri}")
            if count > 10 and count%10 == 1:
                time.sleep(60)
            try: 
                response = requests.get(uri, headers=headers)
                # print(response)
                # print()
                match_str = response.json()
                data = str(match_str)
                if "M'gladbach" in data:
                    data = data.replace("M'gladbach", "Mgladbach")
                    data = data.replace('\'', '"')
                    data = data.replace("Mgladbach", "M'gladbach")
                else:
                    data = data.replace('\'', '"')  
                
                match_list[value[0]].append(data)
                break
                # print(match_list)
            except FileNotFoundError:
                print("matchday data not available")
            count += 1
        print()
    # print(match_list)

    df = pd.DataFrame({'data': match_list})
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
