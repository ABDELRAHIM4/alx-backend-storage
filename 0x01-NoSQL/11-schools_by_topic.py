#!/usr/bin/env python3
"""function that returns the list of school"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school"""
    return (mongo_collection.find({"topics": topic}))
