import json
import logging

import confluent_kafka
from confluent_kafka import Consumer, KafkaException
from Data.KafkaConnection import get_kafka_Consumer
from Data.RedisConnection import exist_in_redis, add_to_reddis
from validator.validator import validate
from Utils.Utils import get_region_with_geopandas, msg_process
from Data.RabbitConnection import get_rabbit_connection

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
    rabbit_connection_channel = get_rabbit_connection()

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
                    alert_dict = msg_process(msg)
                except json.decoder.JSONDecodeError:
                    my_logger(f"alert could not be parse. probably defect | alert: {msg.value()}")

                ## redis
                if not exist_in_redis(alert_dict):
                    add_to_reddis(alert_dict, ttl=REDIS_TTL)
                else:
                    my_logger(f"alert already sent in the last few minutes | {alert_dict}")
                    continue
                ## start validate
                if not validate(alert_dict):
                    my_logger(f"alert could not be validate | {alert_dict}")
                    continue

                else:
                    print("message has been validate")

                ## location
                lon = alert_dict["lon"]
                lat = alert_dict["lat"]
                location_in_charge = get_region_with_geopandas("regions.geojson",lon, lat)
                print(location_in_charge)

                ## rabbit
                rabbit_connection_channel.queue_declare(queue=location_in_charge,
                                                        durable=True,
                                                        arguments={'x-queue-type': 'quorum'})

                rabbit_connection_channel.basic_publish("",
                                                        routing_key=location_in_charge,
                                                        body=json.dumps(alert_dict))
    finally:
        kafka_consumer.close()
        rabbit_connection_channel.close()