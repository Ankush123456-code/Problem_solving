from pymongo import MongoClient
from bson.json_util import dumps
from flask import jsonify, request
import json
import pandas as pd
from pymongo.errors import DuplicateKeyError, BulkWriteError


class Model:
    def __init__(self):
        try:
            self.client = MongoClient(
                "mongodb+srv://Ankush:<password>@cluster0.tpvyynu.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.client.Luigi
            self.task = 0
            self.client.server_info()
        except:
            print("Not success")
        else:
            print("connected")

    def create_collection(self):

        collection_name = f"task_csv"
        existing_collections = self.db.list_collection_names()
        if collection_name in existing_collections:
            return collection_name
        self.db.create_collection(collection_name, capped=True, size=1000000, max=None, autoIndexId=True)
        return collection_name

    def put_one(self, values):
        collections_name = self.create_collection()
        if isinstance(values, dict):
            self.db[collections_name].insert_one(values)
