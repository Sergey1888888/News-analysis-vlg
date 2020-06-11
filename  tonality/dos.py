from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

#pip install dostoevsky
#Просто как вы простили через достаевского

tokenizer = RegexTokenizer()
#tokens = tokenizer.split('всё очень плохо')  # [('всё', None), ('очень', None), ('плохо', None)]

model = FastTextSocialNetworkModel(tokenizer=tokenizer)

#сюда текст
messages = [
    'На сегодняшнем брифинге замглавы облздрава Николай Алимов уточнил, что в инфекционных госпиталях сейчас находятся 1680 пациентов с подтвержденным коронавирусом.',
    'Об этом в среду рассказал зампредседателя комитета здравоохранения Волгоградской области Николай Алимов.'
]

results = model.predict(messages, k=1)

for message, sentiment in zip(messages, results):
    print(sentiment.keys())