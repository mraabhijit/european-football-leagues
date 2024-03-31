from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
import os
from os import path
from dotenv import main
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

print("Started running export_matches_info_to_bq.py ...")

main.load_dotenv()

@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
    BQ_DATASET_NAME = os.getenv('BQ_DATASET_NAME')
    table_id = GCP_PROJECT_ID + '.' + BQ_DATASET_NAME + '.matches_info'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )

print("...successfully ran export_matches_info_to_bq.py")