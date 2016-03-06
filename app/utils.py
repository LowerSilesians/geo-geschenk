import random
import string
import uuid
from bson.json_util import dumps
import json


def random_charts_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def id_generator():
    name = random_charts_generator()
    return uuid.uuid5(uuid.NAMESPACE_DNS, name)


def encode_mongo_data(data=None):
    """
    :return python object
    """
    one = dumps(data)
    two = json.loads(one)
    return two