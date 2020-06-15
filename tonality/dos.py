from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from pymongo import MongoClient
import re

def main():
    client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
    db = client.news
    data = db.analysis
    result = data.find({u'forTonality': True})
    mas = []
    # добавление к analysis поля 'forTonality' чтобы одно и то же не считывать
    # for res in result:
    #     data.update({u'_id': res['_id']}, { u'$set': { 'forTonality': True } }, **{ 'upsert': True })

    def getTonality(messages):
        tokenizer = RegexTokenizer()
        model = FastTextSocialNetworkModel(tokenizer=tokenizer)
        results = model.predict(messages, k=1)
        regex = r"[\w]+\(\['([\w]+)'\]\)"
        mas.clear()
        # результат
        for message, sentiment in zip(messages, results):
            match = re.search(regex, str(sentiment.keys()))
            mas.append(match.group(1))
        return mas

    for arrays in result:
        id = arrays['_id']
        messages = arrays['newsWithMention']
        result = getTonality(messages)
        db.tonality.update({u'_id': id, u'tonality': result}, { u'$setOnInsert': { u'_id': id, u'tonality': result} }, **{ 'upsert': True })
        data.update({u'_id': id}, { u'$set': { u'forTonality': False} }, **{ 'upsert': True })
    
    print('Провека тональносьт завершена')