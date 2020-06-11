import pickle
from string import punctuation
from nltk.corpus import stopwords
from pymystem3 import Mystem
from pyppeteer import launch
from pymongo import MongoClient
from nltk import FreqDist, classify, NaiveBayesClassifier

def lemmatize_sentence(text):
    stop_words = stopwords.words('russian')
    mysteam = Mystem()
    tokens = mysteam.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in stop_words
              and token != " "
              and token.strip() not in punctuation]
    return tokens


    # client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
    # print(client)
    # db = client.news
    # data = db.data
    # browser = await launch({'args': ['--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--ignore-certifcate-errors', '--ignore-certifcate-errors-spki-list', '--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"']})
    # page = await browser.newPage()
    # await page.setViewport({
    #     'width': 1200,
    #     'height': 800
    # })
    # result = data.find({})

if __name__ == "__main__":
     #custom_tweet текст
     custom_tweet = "Замечательный телефон, пользуюсь им уже 2 года, очень нравится"
     custom_tokens = lemmatize_sentence(custom_tweet)
     # filename.pkl модель
     with open('filename.pkl', 'rb') as f:
         classifier = pickle.load(f)
     # сравнение модели
     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
