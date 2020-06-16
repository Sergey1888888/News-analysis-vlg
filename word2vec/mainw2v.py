PATH = '../word2vec/model/kurs_model/'
from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2VecModel
from pprint import pprint
from pymongo import MongoClient
from dbtext import newsToText
import w2v
import os
import sys


client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news


def get_synonyms(elements, count, model, spark_session):
    result = []
    for element in elements:
        a = db.synonyms.insert_one({"word": element})
        try:
            synonyms = model.findSynonyms(element, count).collect()
            for syn in synonyms:
               db.synonyms.update_one({'_id': a.inserted_id },{"$push": {'synom': syn[0] } })
            result.append(synonyms)
        except Exception:
            db.synonyms.update_one({'_id': a.inserted_id },{"$push": {'synom': "Синонимы не найдены" } })
            result.append("Синонимы не найдены")
    print(result)
    return result


def main(word):
    os.chdir("../word2vec")
    if (not os.path.exists('model')):
        if (not os.path.exists('data_text')):
            print("Папка создана")
            os.mkdir('data_text')
        newsToText(db.data)

        word2vec.create_w2v_model()


    spark = SparkSession \
        .builder \
        .appName("SimpleApplication") \
        .getOrCreate()

    model = Word2VecModel.load(PATH)
    
    res = get_synonyms([word],5,model,spark)
    spark.stop()
    os.chdir("../web")
    return res

