if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd


def get_match_points(home_score: int, away_score: int) -> tuple[int, int]:

    if home_score == away_score:
        home_team_points, away_team_points = 1, 1
    elif home_score > away_score:
        home_team_points = 3
        away_team_points = 0
    else:
        home_team_points = 0
        away_team_points = 3
    
    return home_team_points, away_team_points 


def get_goal_difference(home_score: int, away_score: int) -> tuple[int, int]:

    home_gd = home_score - away_score
    away_gd = -home_gd

    return home_gd, -home_gd


leagues = {'Premier League': [38, 10], 
          'Bundesliga': [34, 9], 
          'Ligue 1': [34, 9], 
          'La Liga': [38, 10], 
          'Serie A': [38, 10]}


columns = ['league', 'season', 'league_id', 'season_start_date', 'season_end_date', 
           'matchday', 'match_id', 'match_date', 'home_team', 'away_team', 
           'home_score', 'away_score', 'home_team_points_earned', 'away_team_points_earned', 
           'home_team_gd', 'away_team_gd', 'match_referee']


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = pd.DataFrame(columns = columns)

    for league, total_matchdays in leagues.items():

        print(f"Getting data for {league}...")
        # Get Season, League_id, first and last matchday dates only once as that is a constant
        firstday_data = data[league][0]
        SEASON = int(firstday_data['filters']['season'])
        LEAGUE_ID = firstday_data['competition']['id']
        FIRST_MATCHDAY = firstday_data['matches'][0]['season']['startDate']
        LAST_MATCHDAY = firstday_data['matches'][0]['season']['endDate']
        
        # Also need to consider status
        for mday in range(0, total_matchdays[0]):
            # print(f"\tGetting matchday {mday+1} data...")
            league_data = data[league][mday]

            # No data available for matchday 23 of Serie A :(
            if league == 'Serie A' and mday == 22:
                pass
            else:
                matchday = int(league_data['filters']['matchday'])
            
                for match_num in range(0, total_matchdays[1]):
                    # print(f"\t\tGetting data for match {match_num + 1}")
                    match_data = league_data['matches'][match_num]
                    if match_data['status'] == 'FINISHED':
                        match_id = match_data['id']
                        matchdate = match_data['utcDate']
                        home_team = match_data['homeTeam']['shortName']
                        away_team = match_data['awayTeam']['shortName']
                        home_score = match_data['score']['fullTime']['home']
                        away_score = match_data['score']['fullTime']['away']
                            
                        try:
                            match_referee = match_data['referees'][0]['name']
                        except IndexError:
                            match_referee = ''
                        
                        home_team_points, away_team_points = get_match_points(home_score=home_score, away_score=away_score)
                        
                        # try:
                        home_team_gd, away_team_gd = get_goal_difference(home_score=home_score, away_score=away_score)
                        # except TypeError:
                        #     home_team_gd, away_team_gd = None, None
                            
                        df.loc[len(df.index)] = [league, SEASON, LEAGUE_ID, FIRST_MATCHDAY, LAST_MATCHDAY, 
                                                matchday, match_id, matchdate, home_team, away_team, 
                                                home_score, away_score, home_team_points, away_team_points, 
                                                home_team_gd, away_team_gd, match_referee]

    # Some transformation of datetime columns

    df.season_start_date = pd.to_datetime(df.season_start_date)
    df.season_end_date = pd.to_datetime(df.season_end_date)
    df.match_date = pd.to_datetime(df.match_date).dt.date
    df.match_date = pd.to_datetime(df.match_date)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
