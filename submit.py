from __future__ import unicode_literals

import redis

# fill in the following.
HOST = "redis-18235.c228.us-central1-1.gce.cloud.redislabs.com"
PWD = "w2vwWBPYLIgggR0kiQzkMX7CXN4L1KjC"
PORT = "18235"

redis1 = redis.Redis(host=HOST, password=PWD, port=PORT)

while True:
    key = input("Please enter the key(type 'quit' or 'exit' to end):").strip()
    if key == 'quit' or key == 'exit':
        break
    if key == '':
        continue
    value = input("Please enter the value (type 'quit' or 'exit' to end):").strip()
    # Add your code here

    redis1.set(key, value)
    Y = redis1.get(key)
    print(Y)