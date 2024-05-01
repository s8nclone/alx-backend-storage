#!/usr/bin/env python3
"""
Function to list all entries
"""


def schools_by_topic(mongo_collection, topic):
    """
     returns the list of school having a specific topic

    :param mongo_collection:
    :param topic:
    :return:
    """
    return mongo_collection.find({"topics": topic})
