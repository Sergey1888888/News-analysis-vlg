from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from pymongo import MongoClient
import re

client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news
data = db.analysis
result = data.find()

def getTonality(messages):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    results = model.predict(messages, k=1)
    regex = r"[\w]+\(\['([\w]+)'\]\)"
    # результат
    for message, sentiment in zip(messages, results):
        match = re.search(regex, str(sentiment.keys()))
        return match.group(1)

for arrays in result:
    id = arrays['_id']
    messages = arrays['newsWithMention']
    result = getTonality(messages)
    db.testik.insert({u'_id': id, u'tonality': result}, {u'$setOnInsert': {u'_id': id, u'tonality': result}, **{u'upsert': True}})