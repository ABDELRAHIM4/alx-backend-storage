#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """method using the __qualname__ dunder method."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return (wrapper)

class Cache():
    """Create a Cache class. In the __init__ method"""
    def __init__(self):
        """store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """decorator that takes a single method Callable"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """method using the __qualname__ dunder method."""
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return (wrapper)
    def call_history(method):
        """call_history decorator to store the history of inputs"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """wraps method for call_history"""
            input_list = "{}:inputs".format(method.__qualname__)
            output_list = "{}:outputs".format(method.__qualname__)
            self._redis.rpush(input_list, str(args))
            out = method(self, *args, **kwargs)
            self._redis.rpush(output_list, str(out))
            return (out)
        return (wrapper)
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
    def get(self, key: str, fn: Callable[[bytes], any] = lambda x: x) -> any:
        """create a get method that take a key"""
        des = self._redis.get(key)
        if des is None:
            return (None)
        return (fn(des))
    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get"""
        return self.get (key, lambda x: x.decode("utf-8"))
    def get_int(self, key: str) -> str:
        """automatically parametrize Cache.get"""
        return self.get(key, int)
    def replay(method: Callable):
        """implement a replay function to display the history of calls of a particular function"""
        r = redis.Redis()
        methods = method.__qualname__
        intput = f"{methods}: inputs"
        output = f"{methods}:outputs"
        
        intp = r.lrange(intput, 0, -1)
        outp = r.lrange(output, 0, -1)
        print(f"{methods} was called {intp} times:")
        for i, p in zip(intp, outp):
            print(f"{methods}(*(eval(i,)) -> {p.decode('utf-8')}")
