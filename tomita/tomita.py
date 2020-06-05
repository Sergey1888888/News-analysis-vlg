from pymongo import MongoClient
from bson.json_util import loads, dumps
import subprocess
import re

def find_document(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news
collection = db.data
print(collection)
posts = db.data

result = find_document(posts, {'forAnalysis': False}, True)
# запись текста новостей в файл для томиты
f = open('input.txt', 'w')
for text in result:
    f.write(text.get("newsText")+'\n')

f.close()

# запуск томиты и получение данных
p = subprocess.Popen(["tomita-parser", "config.proto"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
out = out.decode("utf-8", "strict")


result = re.findall(r'(Person|Attractions)[\n\s{]*(FIO[\s=а-яёА-яa-zA-Z0-9]+|Name[\s=а-яА-яёa-zA-Z0-9]+)(Text[\s=а-яА-яёa-z0-9№A-Z,!.?\"\-—–]+)',out )

for fact in result:
    
    if fact[0] == 'Person':
        a = fact[1][6:-3]
    elif  fact[0] == 'Attractions':
        a = fact[1][7:-3]
    b = a.split(' ')
    str = '_'.join(b)
    c = fact[2][7:-2]
    mystr = c.replace(a,str)
    print(mystr)
    print("\n")

