from azure.devops.released.work_item_tracking import WorkItemTrackingClient, \
    Wiql, JsonPatchOperation, WorkItemRelation
from msrest.authentication import BasicAuthentication

import logging


def convert_document(command):
    return [JsonPatchOperation(op=x['op'], path=x['path'], value=x['value'])
            for x in command['document']]


class AdoClient:
    client = None
    project_name = ""

    def __init__(self, base_url=None, pat=None, project_name=None):
        self.client = WorkItemTrackingClient(
            base_url, BasicAuthentication('', pat))
        self.project_name = project_name

    def write_changes(self, operation):
        create = operation.get('create', None)
        if (create != None):
            logging.info('Creating work item')
            res = self.client.create_work_item(document=convert_document(create),
                                               project=self.project_name,
                                               type=create['type'])
            logging.info(f'Work item created: {res.id}')
            return res.id

        update = operation.get('update', None)
        if (update != None):
            id = update['id']
            logging.info(f'Updating work item {id}')
            res = self.client.update_work_item(
                document=convert_document(update), id=id)
            logging.info(f'Work item {id} updated {res.id}')
            return res.id
