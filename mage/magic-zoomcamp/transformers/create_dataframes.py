if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


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

    df_matches = data[['match_id', 'home_team', 'away_team', 'home_score', 
    'away_score', 'home_team_points_earned', 'away_team_points_earned', 'home_team_gd', 'away_team_gd']]

    columns_match_info = ['league', 'league_id',
       'matchday', 'match_id', 'match_date',
       'match_referee']

    df_match_info = data[columns_match_info]

    df_seasons =  data[['league_id', 'season', 'season_start_date', 'season_end_date']]
    df_seasons = df_seasons.drop_duplicates(subset='league_id', keep='first', ignore_index=True)

    print(df_matches.head())
    print()
    print(df_match_info.head())
    print()
    print(df_seasons)

    return df_matches, df_match_info, df_seasons


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
