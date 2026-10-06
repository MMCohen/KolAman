import datetime

import confluent_kafka
import json

source_list = ["aman", "mossad", "pikud-haoref", "shabak"]
priority_list = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
classification_list = ["UNCLASSIFIED", "RESTRICTED", "SECRET", "TOP_SECRET"]

def msg_process(msg: confluent_kafka.cimpl.Message):
    """
    gets plain kafka msg and try to convert it to dict
    """
    value = msg.value().decode()

    text_dict = json.loads(value)

    return text_dict


def validat_source(processed_message) -> bool:
    """
    verify that title is one of title_list
    :param processed_message:
    :return:
    """
    if processed_message["source"] not in source_list:
        return False
    return True


def validat_title(processed_message):
    return True


def validat_priority(processed_message):
    if processed_message["priority"] not in priority_list:
        return False
    return True

def validat_classification(processed_message):
    if processed_message["classification"] not in classification_list:
        return False
    return True


def validat_lon_and_lat(processed_message):
    try:
        lon = float(processed_message["lon"])
        lat = float(processed_message["lat"])

    except ValueError:
        return False

    if lon > 90 or lon < -90 or lat > 180 or lat < -180:
        return False
    return True


def validat_timestamp(processed_message):
    try:
        date = datetime.datetime.strptime(processed_message["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
    except:
        print("problem")
        return False
    return True

def validate(msg: dict) -> bool:
    try:
        if not validat_source(msg):
            return False

        if not validat_title(msg):
            return False

        if not validat_priority(msg):
            return False

        if not validat_classification(msg):
            return False

        if not validat_lon_and_lat(msg):
            return False

        if not validat_timestamp(msg):
            return False

        return True

    except KeyError:
        print(f"field is mising in the alert | {msg}") ## todo: change to logger
        return False

    finally:
        print("goodbye")


if __name__ == "__main__":
    x = confluent_kafka.cimpl.Message(value=b'{\n  "alert_id": "c4424e25-aa12-45e0-bae7-7f90e7c76f6e",\n  "source": "pikud-haoref",\n  "title": "\\u05d4\\u05ea\\u05e8\\u05e2\\u05d4 \\u05de\\u05e7\\u05d3\\u05d9\\u05de\\u05d4",\n  "content": "\\u05d1\\u05d3\\u05e7\\u05d5\\u05ea \\u05d4\\u05e7\\u05e8\\u05d5\\u05d1\\u05d5\\u05ea \\u05e6\\u05e4\\u05d5\\u05d9\\u05d5\\u05ea \\u05dc\\u05d4\\u05ea\\u05e7\\u05d1\\u05dc \\u05d4\\u05ea\\u05e8\\u05e2\\u05d5\\u05ea \\u05d1\\u05d0\\u05d6\\u05d5\\u05e8 \\u05db\\u05e4\\u05e8 \\u05e1\\u05d1\\u05d0. \\u05d9\\u05e9 \\u05dc\\u05d4\\u05ea\\u05e7\\u05e8\\u05d1 \\u05dc\\u05de\\u05e8\\u05d7\\u05d1 \\u05de\\u05d5\\u05d2\\u05df.",\n  "priority": "HIGH",\n  "classification": "UNCLASSIFIED",\n  "lat": 32.1764,\n  "lon": 34.9037,\n  "timestamp": "2026-10-05T14:00:14.196Z",\n  "status": "WAITING"\n}\n')
    print(validate(x))

    # x = datetime.datetime.strptime("2026-10-05T14:00:14.196Z", "%Y-%m-%dT%H:%M:%S.%fZ")
    # print(x)

