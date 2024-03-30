if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

print("Started running transform_matches_table.py ...")

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df_matches = data[['match_id', 'home_team', 'away_team', 'home_score', 
    'away_score', 'home_team_points_earned', 'away_team_points_earned', 'home_team_gd', 'away_team_gd']]

    return df_matches

print("...successfully ran transform_matches_table.py")

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
