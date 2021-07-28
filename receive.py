import json
import os

import pika
import sys

from pika.exceptions import IncompatibleProtocolError

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
        newIssues = json.load(body.decode())
        print(newIssues)
        print(f"Count Issues: {len(newIssues)}")
        for item in newIssues:
            print(f"id: {item['issue.is']}")

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
