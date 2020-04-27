import logging
from .ado_client import AdoClient
import azure.functions as func
import os
import json


def main(req: func.HttpRequest) -> func.HttpResponse:

    base_url = os.environ['ADO_BASE_URL']
    creds = os.environ['ADO_CREDENTIAL']
    project_name = os.environ['ADO_PROJECT_NAME']

    client = AdoClient(base_url, creds, project_name)
    item_id = client.write_changes(req.get_json())
    return func.HttpResponse(json.dumps({"status": "ok", "id": item_id}), mimetype='application/json')
