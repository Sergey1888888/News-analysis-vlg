from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from pymongo import MongoClient
import re

# client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
# db = client.news
# data = db.analysis
# result = data.find({})

tokenizer = RegexTokenizer()
#tokens = tokenizer.split('всё очень плохо')  # [('всё', None), ('очень', None), ('плохо', None)]

model = FastTextSocialNetworkModel(tokenizer=tokenizer)

#сюда текст
messages = [
    'На сегодняшнем брифинге замглавы облздрава Николай Алимов уточнил, что в инфекционных госпиталях сейчас находятся 1680 пациентов с подтвержденным коронавирусом.',
    'Об этом в среду рассказал зампредседателя комитета здравоохранения Волгоградской области Николай Алимов.',
    'Я тебя люблю!'
]

results = model.predict(messages, k=1)

regex = r"[\w]+\(\['([\w]+)'\]\)"
# результат
for message, sentiment in zip(messages, results):
    match = re.search(regex, str(sentiment.keys()))
    print(match.group(1))