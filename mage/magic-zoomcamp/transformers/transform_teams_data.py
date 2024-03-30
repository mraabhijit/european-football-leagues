if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

print("Started running transform_teams_data.py ...")

import pandas as pd

league_teams = {"Premier League": 20, 
        "Bundesliga": 18,
        "Ligue 1": 18,
        "La Liga": 20,
        "Serie A": 20}

df = pd.DataFrame(columns = ['team_id', 'team', 'full_name', 'abbv', 
                             'team_crest', 'address', 'country', 'year_founded', 
                             'stadium', 'coach', 'coach_nationality'])

@transformer
def transform(data, *args, **kwargs):
    for league, value in league_teams.items():
        print(f"Adding teams of {league}...")
        # print("-"*50)
        for i in range(value):
            league_data = data[league][i]
            team_id = league_data['id']
            team = league_data['shortName']
            full_name = league_data['name']
            abbv = league_data['tla']
            team_crest = league_data['crest']
            address = league_data['address']
            country = league_data['area']['name']
            year_founded = league_data['founded']
            stadium = league_data['venue']

            # if league_data['coach']['lastName'] != '':
            #     coach = (league_data['coach']['firstName'] + ' ' + league_data['coach']['lastName']).strip()
                
            coach = str(league_data['coach']['firstName']) + " " + str(league_data['coach']['lastName'])
            coach = coach.strip()

            coach_nationality = league_data['coach']['nationality']

            df.loc[len(df.index)] = [team_id, team, full_name, abbv, team_crest, address, country, year_founded, stadium, coach, coach_nationality]

    print("...successfully ran transform_teams_data.py")
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
