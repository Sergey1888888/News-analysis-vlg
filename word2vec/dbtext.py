import os
from pymongo import MongoClient
def newsToText(data):
    if not os.path.isdir('data_news'):
        os.mkdir("data_news")

    i = 0
    for text in data.find():
        f2 = open('data_news/input'+str(i)+'.txt', 'w')  
        f2.write(text.get("newsText"))
        f2.close()
        i = i +1



