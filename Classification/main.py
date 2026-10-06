import json
import logging

import confluent_kafka
from confluent_kafka import Consumer, KafkaException
from Data.KafkaConnection import get_kafka_Consumer
from Data.RedisConnection import exist_in_redis, add_to_reddis
from validator.validator import validate
from Utils.Utils import get_region_with_geopandas, msg_process

REDIS_TTL = 300

def my_logger(text: str):
    """placeholder for logs"""
    print(text)
    pass


if __name__ == "__main__":

    # logging.basicConfig(filename="newfile.log",
    #                     format='%(asctime)s %(levelname)s: %(message)s',
    #                     filemode='a')
    #
    # logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)
    #
    # logger.debug("Harmless debug message")
    # logger.info("Just an information")
    # logger.warning("Its a warning")
    # logger.error("Did you try to divide by zero?")
    # logger.critical("Internet is down")

    try:
        kafka_consumer = get_kafka_Consumer()

        while True:
            kafka_consumer.subscribe(["topic"])
            msg = kafka_consumer.poll(timeout=1.0)
            if msg is None:
                print("waiting for messages")
                continue

            if msg.error():
                raise KafkaException(msg.error())

            ## Start to consume messages
            else:
                ## try to convert to dict
                try:
                    msg_dict = msg_process(msg)
                except json.decoder.JSONDecodeError:
                    my_logger(f"alert could not be parse. probably defect | alert: {msg.value()}")

                ## redis
                if not exist_in_redis(msg_dict):
                    add_to_reddis(msg_dict, ttl=REDIS_TTL)
                else:
                    my_logger(f"alert already sent in the last few minutes | {msg_dict}")
                    continue
                ## start validate
                if not validate(msg_dict):
                    my_logger(f"alert could not be validate | {msg_dict}")
                    continue

                else:
                    print("message has been validate")

                ##
    finally:
        kafka_consumer.close()