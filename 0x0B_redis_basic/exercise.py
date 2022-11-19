#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4, UUID
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Create and return function that increments the count for that key
    every time the method is called and returns the value returned by
    the original method..
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Function wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Create and return function that increments the count for that key
    every time the method is called and returns the value returned by
    the original method.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Function wrapper
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(fn: Callable):
    """
    Function to display the history of calls of a particular function.
    """
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{f_name}(*{i}) -> {o}')


class Cache:
    """
    Create a Cache class. In the __init__ method,
    store an instance of the Redis client as a
    private variable named _redis (using redis.
    Redis()) and flush the instance using flushdb
    """
    def __init__(self):
        """
        Function constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method that takes a data argument and returns a string
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get method that take a key string argument and an optional
        Callable argument named fn
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """
        Reading from Redis and recovering original type
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        Reading from Redis and recovering original type
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
