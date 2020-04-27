import logging
import json
from __app__.shared_code.rabbit.utils.config import CHANNEL_DURABLE, PUBLISH_PROPERTIES
from __app__.shared_code.rabbit.utils.queue_name import MAPPING_QUEUE
from __app__.shared_code.rabbit.utils.utils import RabbitConnectionFactory
from opencensus.ext.azure.log_exporter import AzureLogHandler
import os
import azure.functions as func

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey='+os.environ['APPINSIGHTS_INSTRUMENTATIONKEY']))


def main(req: func.HttpRequest) -> func.HttpResponse:
    user_id = req.params.get('user_id')
    profile_id = req.params.get('profile_id')
    logger.info(f'Received request userId={user_id}'
                f' sync_profile_id={profile_id}')

    try:
        with RabbitConnectionFactory.get_connection() as connection:
            message = prepare_message(req.get_json(), user_id, profile_id)
            channel = connection.channel()
            channel.queue_declare(queue=MAPPING_QUEUE,
                                  durable=CHANNEL_DURABLE)
            channel.basic_publish(exchange='',
                                  routing_key=MAPPING_QUEUE,
                                  body=json.dumps(message),
                                  properties=PUBLISH_PROPERTIES)

            logger.info("Message sent to mapping queue")
    except Exception as ex:
        logger.error(ex)
        return func.HttpResponse('{"status": "error"}', status_code=200)

    return func.HttpResponse('{"status": "ok"}', status_code=200)


def prepare_message(body, user_id, sync_profile_id):
    return {
        'body': body,
        'user_id': user_id,
        'sync_profile_id': sync_profile_id,
    }
