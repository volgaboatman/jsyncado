import os
import pika

CHANNEL_DURABLE = True
CONSUMER_AUTO_ACK = False
EXCHANGE_TYPE = 'topic'
PUBLISH_PROPERTIES = pika.BasicProperties(
    delivery_mode=2,  # make message persistent
)


RABBIT_HOST = os.getenv('RABBIT_HOST', '165.22.76.42')
RABBIT_PORT = os.getenv('RABBIT_PORT', '5672')
RABBIT_USER = os.getenv('RABBIT_USER', 'adojira')
RABBIT_PASS = os.getenv('RABBIT_PASS', 'adojirapwd')


def get_secret_file(key: str):
    try:
        with open(key) as secret_file:
            return secret_file.readline()
    except FileNotFoundError:
        return None


def read_secrets():
    global RABBIT_USER  # pylint: disable=global-statement
    global RABBIT_PASS  # pylint: disable=global-statement
    user = get_secret_file('.rabbit.user')
    if user is not None:
        RABBIT_USER = user
    user = get_secret_file('/run/secrets/rabbit_user')
    if user is not None:
        RABBIT_USER = user

    password = get_secret_file('.rabbit.pass')
    if password is not None:
        RABBIT_PASS = password
    password = get_secret_file('/run/secrets/rabbit_pass')
    if password is not None:
        RABBIT_PASS = password


read_secrets()
