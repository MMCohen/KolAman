import pika

def get_rabbit_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    return channel

if __name__ == "__main__":

    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # channel = connection.channel()

    # channel.queue_declare(queue='try2', durable=True, arguments={'x-queue-type': 'quorum'})

    # channel.basic_publish(exchange='',
    #                       routing_key='try2',
    #                       body='Hello 3!')
    # print(" [x] Sent 'Hello World!'")
    pass