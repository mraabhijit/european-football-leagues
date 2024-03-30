from mage_ai.orchestration.triggers.api import trigger_pipeline
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

print("Triggering pipeline: ingest_data_to_data_lake_teams.py ...")

@data_loader
def trigger(*args, **kwargs):
    """
    Trigger another pipeline to run.

    Documentation: https://docs.mage.ai/orchestration/triggers/trigger-pipeline
    """

    trigger_pipeline(
        'ingest_data_to_data_lake_teams',        # Required: enter the UUID of the pipeline to trigger
        variables={'env': 'default'},           # Optional: runtime variables for the pipeline
        check_status=True,     # Optional: poll and check the status of the triggered pipeline
        error_on_failure=False, # Optional: if triggered pipeline fails, raise an exception
        poll_interval=60,       # Optional: check the status of triggered pipeline every N seconds
        poll_timeout=None,      # Optional: raise an exception after N seconds
        verbose=True,           # Optional: print status of triggered pipeline run
    )
