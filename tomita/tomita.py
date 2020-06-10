from pymongo import MongoClient
import subprocess
import re
import sys
from per_attract_to_txt import checkPersons, checkPlaces

def tomita(db):

    textForAnalysis = db.data.find({"forAnalysis": True})
    if textForAnalysis.count(True) > 0:

        i = 0
        for fact in textForAnalysis:
            print(i)
            i = 1+i
            f = open('input.txt', 'w')
            f.write(fact.get("newsText"))
            f.close()
            p = subprocess.Popen(["tomita-parser", "config.proto"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            out = out.decode("utf-8", "strict")
            result = re.findall(r'(Person|Attractions)[\n\s{]*(FIO[\s=а-яёА-яa-zA-Z0-9]+|Name[\s=а-яА-яёa-zA-Z0-9]+)(Text[\s=а-яА-яёa-z0-9№A-Z,!.?\"\-—–]+)',out )
            b.data.update_one({"_id": fact.get("_id")},{"$set":{"forAnalysis": False}})

            if not result:
                continue
            
            if result[0][0] == 'Person':
                a = result[0][0]
            elif  result[0][0] == 'Attractions':
                a = result[0][0]

            c = result[0][2][7:-2]
            db.analysis.insert_one({'_id': fact.get('_id'),'newsWithMention': c})
            
    else: 
        print('Нету новый новостей')

def check(parameter_list):
    pass
if __name__ == '__main__':
    client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
    db = client.news
    checkPersons(db)
    checkPlaces(db)
    tomita(db)