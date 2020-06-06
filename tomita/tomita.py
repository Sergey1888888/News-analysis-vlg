from pymongo import MongoClient
import subprocess
import re
import sys
sys.path.append("..")
from modeldb import Connection, Mongo

conn = Connection('45.11.24.111', 27017, 'passw0rd', 'mongo-root').getConnection()
db = Mongo(conn,'news')

textForAnalysis = db.find_document('data', {'forAnalysis': False}, True)

# запись текста новостей в файл для томиты
f = open('input.txt', 'w')
for text in textForAnalysis:
   
    f.write(text.get("newsText")+'\n')

f.close()

# запуск томиты и получение данных
p = subprocess.Popen(["tomita-parser", "config.proto"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
out = out.decode("utf-8", "strict")


result = re.findall(r'(Person|Attractions)[\n\s{]*(FIO[\s=а-яёА-яa-zA-Z0-9]+|Name[\s=а-яА-яёa-zA-Z0-9]+)(Text[\s=а-яА-яёa-z0-9№A-Z,!.?\"\-—–]+)',out )
facts = []
for fact in result:
    if fact[0] == 'Person':
        a = fact[1][6:-3]
    elif  fact[0] == 'Attractions':
        a = fact[1][7:-3]
    b = a.split(' ')
    str = '_'.join(b)
    c = fact[2][7:-2]
    mystr = c.replace(a,str)
    facts.append({'newsWithMention': mystr})

db.insert_document('test',facts,True)