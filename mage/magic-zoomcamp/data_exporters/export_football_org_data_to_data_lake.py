from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import os
from os import path
from dotenv import main

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

print("Started running export_football_org_data_to_data_lake.py...")

main.load_dotenv()

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = os.getenv('STORAGE_BUCKET_NAME')
    object_key = 'matches.parquet'

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
        # format = 'json'
    )

    print("...successfully ran export_football_org_data_to_data_lake.py")

# Export the DataFrame as a JSON file to GCS
# gcs_loader.export(df, bucket_name='your_bucket_name', object_key='your_object_key.json', format='json')