import confluent_kafka
from confluent_kafka import Consumer, KafkaException

def get_kafka_Consumer():
    conf = {'bootstrap.servers': 'localhost:9092',
            'group.id': 'Classification',
            'auto.offset.reset': 'earliest'}

    consumer = Consumer(conf)

    return consumer
