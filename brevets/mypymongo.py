import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.lists

def brevet_insert(start_time, brevet_dist, checkpoints):
    output = collection.insert_one({
        "start_time": start_time,
        "brevet_dist": brevet_dist,
        "checkpoints": checkpoints})
    _id = output.inserted_id
    return str(_id)


def brevet_find():
    lists = collection.find().sort("_id", -1).limit(1)
    for brevet_list in lists:
        return brevet_list["start_time"], brevet_list["brevet_dist"], brevet_list["checkpoints"]
