import pika
from .config import RABBIT_USER, RABBIT_PASS, RABBIT_HOST, RABBIT_PORT


class RabbitConnectionFactory:

    _credentials = pika.PlainCredentials(username=RABBIT_USER,
                                         password=RABBIT_PASS)

    _params = pika.ConnectionParameters(host=RABBIT_HOST,
                                        port=RABBIT_PORT,
                                        credentials=_credentials)

    @staticmethod
    def get_connection():
        return pika.BlockingConnection(RabbitConnectionFactory._params)


class ChannelTX:
    def __init__(self, channel) -> None:
        self._channel = channel
        super().__init__()

    def __enter__(self):
        self._channel.tx_select()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, Exception):
            self._channel.tx_rollback()
        else:
            self._channel.tx_commit()
