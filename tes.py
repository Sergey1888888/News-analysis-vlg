from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news
l = db.analysis.find_one({"_id": ObjectId('5ee164c31dd8a693e3f6fedd')}).get("newsWithMention")
for a in l:
    print(a)