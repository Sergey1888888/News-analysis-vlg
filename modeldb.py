from pymongo import MongoClient
from bson.objectid import ObjectId

class Connection:
    conn = None

    def __init__(self, host='localhost', pt= 27017, pwd= None, usrname = None):
        self.conn = MongoClient(host, port=pt , password = pwd, username = usrname)  # можно и не передавать, тут по умолчанию эти данные

    def getConnection(self):
        return self.conn


class Mongo:
    db = None

    def __init__(self, connection, databaseName):
        self.db = connection[databaseName]

    def table(self, collectionName: str):
        return self.db[collectionName]

    def insert_document(self, collectionName, data,multiple=False):
        collection = self.db[collectionName]
        print("Добавляем в бд")
        if multiple:
            return collection.insert_many(data)
        else:
            return collection.insert_one(data)
     
    def find_document(self, collectionName, data, multiple=False):
        collection = self.db[collectionName]
        print("Ищем в бд")
        if multiple:
            results = collection.find(data)
            return [r for r in results]
        else:
            return collection.find_one(data)

    def replaceById(self, collectionName, id ,newData ):
        collection = self.db[collectionName]
        print("Заменяем в бд")
        collection.replace_one({'_id': ObjectId(id)}, newData )  # ух сложненько и не робит




