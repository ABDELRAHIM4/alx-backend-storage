#!/usr/bin/env python3
"""Python script that provides some stats"""
import pymongo


def log_st():
    """Python script that provides some stats"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    Collection = client.logs.nginx
    docum = Collection.count_documents({})
    print(f"{docum} logs")
    print("Methods")
    for meth in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        num = Collection.count_documents({"method": meth})
        print(f"{meth}: {num}")
    add = Collection.count_documents({ "method" : "GET", "path": "/status"})
    print(f"{add} status check")

if __name__ == "__main__":
    log_st()
