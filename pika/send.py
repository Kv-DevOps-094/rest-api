import pika

RABBIT_HOST = 'localhost'
QUEUE = 'hello'

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST))
channel = connection.channel()

channel.queue_declare(queue=QUEUE)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello world!')
print("[x] Sent 'Hello world!'")

connection.close()