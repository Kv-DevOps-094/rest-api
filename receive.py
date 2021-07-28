import json
import os
from types import SimpleNamespace

import pika
import sys

from pika.exceptions import IncompatibleProtocolError

from commands import parseJson, addUser, addIssueActionLabelState, addIssueActionState

RABBIT_HOST = '15.237.25.152'
RABBIT_PORT = '5672'
RABBIT_LOGIN = 'devops'
RABBIT_PASSWORD = 'softserve'
RABBIT_QUEUE = 'restapi'


def main():
    credentials = pika.PlainCredentials(username=RABBIT_LOGIN, password=RABBIT_PASSWORD)

    parameters = pika.ConnectionParameters()
    parameters.host = RABBIT_HOST
    parameters.port = RABBIT_PORT
    parameters.virtual_host
    parameters.credentials = credentials

    def callback(ch, method, properties, body):

        addUser(body.decode())
        # Add data from new issue
        # addIssueActionLabelState(body)
        #
        # addUser(body)
        # # Add changed status for issue
        addIssueActionState(body.decode())

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=RABBIT_QUEUE)
    channel.basic_consume(RABBIT_QUEUE, callback)
    print(' [*] Waiting for message. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            exit(0)
