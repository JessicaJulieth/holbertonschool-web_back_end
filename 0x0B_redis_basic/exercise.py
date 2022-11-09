#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Create and return function that increments the count for that key
    every time the method is called and returns the value returned by
    the original method..
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args, **kwargs):
        ke = method(self, *args, **kwargs)
        self._redis.incr(key)
        return ke

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Create and return function that increments the count for that key
    every time the method is called and returns the value returned by
    the original method.
    """
    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(in_key, str(args))
        res = method(self, *args)
        self._redis.rpush(out_key, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """
    Function to display the history of calls of a particular function.
    """
    client = redis.Redis()
    st_name = Cache.store.__qualname__

    inputs = client.lrange("{}:inputs".format(st_name), 0, -1)
    outputs = client.lrange("{}:outputs".format(st_name), 0, -1)

    print("{} was called {} times:".format(st_name,
          client.get(st_name).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(st_name, i.decode("utf-8"),
              o.decode("utf-8")))


class Cache:
    """
    Create a Cache class. In the __init__ method,
    store an instance of the Redis client as a
    private variable named _redis (using redis.
    Redis()) and flush the instance using flushdb
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method that takes a data argument and returns a string
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get method that take a key string argument and an optional
        Callable argument named fn
        """
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)
