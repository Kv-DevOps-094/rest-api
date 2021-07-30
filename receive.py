import sys
import pika
from commands import parseJson, addIssueActionLabelStateCommands, addIssueActionState, isIssueExist
from config import *
from db import dbSession

# RABBIT_HOST = '15.237.25.152'
# RABBIT_PORT = '5672'
# RABBIT_LOGIN = 'devops'
# RABBIT_PASSWORD = 'softserve'
# RABBIT_QUEUE = 'restapi'


def main():
    """RabbitMQ integration Component"""
    credentials = pika.PlainCredentials(username=RABBIT_USER, password=RABBIT_PW)
    parameters = pika.ConnectionParameters()
    parameters.host = RABBIT_HOST
    parameters.port = RABBIT_PORT
    # parameters.virtual_host
    parameters.credentials = credentials

    def callback(ch, method, properties, body):
        data = parseJson(body.decode())
        if data.action == 'opened':
            addIssueActionLabelStateCommands(body.decode())
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
