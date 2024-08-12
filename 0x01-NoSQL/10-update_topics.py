#!/usr/bin/env python3
"""Python function that changes all topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of a school"""
    return (mongo_collection.update_many({"name": name} ,{"$set": { "topics": topics}}))
