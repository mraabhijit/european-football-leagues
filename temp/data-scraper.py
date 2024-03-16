import requests
import json
import pandas as pd

uri = 'https://api.football-data.org/v4/matches'

# function to read api-key
def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys(".secret/football-data.json")
headers = { 
    'X-Auth-Token': keys["X-Auth-Token"] 
}

matches = {}
response = requests.get(uri, headers=headers)
for i, match in enumerate(response.json()['matches']):
  matches[i] = match

with open("matches.json", "w") as f_out:
  f_out.write(str(matches))

