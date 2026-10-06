import time

import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def exist_in_redis(msg: dict) -> bool | None:
    try:
        return bool(r.exists(msg["alert_id"]))
    except KeyError:
        return None


def add_to_reddis(msg: dict, ttl: int) -> bool:
    try:
        r.set(msg["alert_id"], str(msg), ex=ttl)
        return True
    except KeyError:
        return False


if __name__ == "__main__":
    print("hello fro, redis conection")

    r.set('foo', 'bar', ex=1)
    # True
    time.sleep(2)
    print(bool(r.exists('foo')))
    # print(r.ttl('foo'))
    # time.sleep(2)
    # print(r.ttl('foo'))



    # print(r.exists('foo'))
    # print(bool(r.exists('foo')))
    # print(r.get("foo"))

