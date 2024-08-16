#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method"""
import redis
import uuid


class Cache():
    """Create a Cache class. In the __init__ method"""
    def __init__(self):
        """store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """method that takes a data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
