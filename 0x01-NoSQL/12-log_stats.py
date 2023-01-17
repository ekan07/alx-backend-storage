#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    this function provides some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        documents = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, documents))
    status = mongo_collection.count_documents({"method": "GET",
                                              "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        log_stats(collection)
