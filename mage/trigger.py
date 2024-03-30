import os
import requests

class MageTrigger:
    OPTIONS = {
      "ingest_data_to_data_lake": {
        "trigger_id": 10, 
        "key": "f3a1a4228fc64cfd85295b668c93f3b2"
        }
    }


    @staticmethod
    def trigger_pipeline(pipeline_name, variables=None):
        trigger_id = MageTrigger.OPTIONS[pipeline_name]["trigger_id"]
        key = MageTrigger.OPTIONS[pipeline_name]["key"]

        endpoint = f"http://localhost:6789/api/pipeline_schedules/{trigger_id}/pipeline_runs/{key}"
        headers = {'Content-Type': 'application/json'}
        payload = {}

        if variables is not None:
            payload['pipeline_run'] = {'variables': variables}

        response = requests.post(endpoint, headers=headers, json=payload)
        return response

MageTrigger.trigger_pipeline("ingest_data_to_data_lake")