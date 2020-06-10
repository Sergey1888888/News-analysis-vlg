from pymongo import MongoClient
import os
client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news
data = db.data

 if not os.path.isdir('data_news'):
    os.mkdir("data_news")

i = 0 
for text in data.find({"forAnalysis": True}):
    f2 = open('data_news/input'+str(i)+'.txt', 'w')  
    f2.write(text.get("newsText"))
    f2.close()
    i = i +1

