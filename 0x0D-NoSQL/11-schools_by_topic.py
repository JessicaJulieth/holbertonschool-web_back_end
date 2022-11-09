#!/usr/bin/python3
"""
Where can I learn Python?
"""
def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of school having a specific topic
    """
    doc = mongo_collection.find({"topics": topic})
    lists = [i for i in doc]
    return lists
