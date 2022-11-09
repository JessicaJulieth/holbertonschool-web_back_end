#!/usr/bin/env python3
"""
Log stats - new version
"""

from pymongo import MongoClient


if __name__ == "__main__":
    coll = MongoClient("mongodb://127.0.0.1:27017").logs.nginx
    print(f'{coll.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {coll.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {coll.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {coll.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {coll.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {coll.count_documents({"method": "DELETE"})}')
    print(f'{coll.count_documents({"path": "/status"})} status check')
    print('IPs:')
    ips = coll.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])
    for ip in ips:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')
