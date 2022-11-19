#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Python script that provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    coll = client.logs.nginx
    print("{} logs".format(coll.estimated_document_count()))
    print("Methods:")
    print("\tmethod GET: {}".format(coll.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(coll.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(coll.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(coll.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(coll.count_documents({"method": "DELETE"})))
    print("{} status check".format(coll.count_documents({"path": "/status"})))
