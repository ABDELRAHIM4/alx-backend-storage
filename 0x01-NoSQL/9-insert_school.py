#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based"""


def insert_school(mongo_collection, **kwargs):
    """Python function that inserts a new document"""
    return (mongo_collection.insert_one(kwargs).inserted_id)
