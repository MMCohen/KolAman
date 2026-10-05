import json

import confluent_kafka
from confluent_kafka import Consumer, KafkaException
from Data.KafkaConnection import get_kafka_Consumer
from Data.Redis_connection import exist_in_redis, add_to_reddis
from validator.validator import validate
from Utils.Utils import get_region_with_geopandas



if __name__ == "__main__":
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
            else:
                if not exist_in_redis(msg.value()):
                    add_to_reddis(msg)

                if validate(msg):
                    print("message has been validate")

                location = get_region_with_geopandas("regions.geojson",34.800, 32.100 )
                print(location)
    finally:
        kafka_consumer.close()