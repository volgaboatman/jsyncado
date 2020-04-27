import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    user_id = req.params.get('user_id')
    profile_id = req.params.get('profile_id')
    logging.info(f'Received request userId={user_id}'
                 f' sync_profile_id={profile_id}')
    logging.info(req.get_json())

    return func.HttpResponse("", status_code=200)
