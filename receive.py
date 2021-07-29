import json
import os
from types import SimpleNamespace

import pika
import sys

from pika.exceptions import IncompatibleProtocolError

from commands import parseJson, addUser, addIssueActionLabelState, addIssueActionState, isIssueExist
from db import dbSession

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
        data = parseJson(body.decode())
        if data.action == 'opened':
            addIssueActionLabelState(body.decode())
            print(f"{data.issue.id} is {data.action} added")
        else:
            if isIssueExist(data.issue.id):
                sessionAddIssueActionState = dbSession()
                sessionAddIssueActionState.expire_on_commit = False
                addIssueActionState(body.decode())
                print(f"{data.issue.id} is {data.action} updated")
            else:
                print(f"{data.issue.id} not found")

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
