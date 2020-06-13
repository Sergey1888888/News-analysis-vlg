from flask import Flask, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news


@app.route('/')
def index():
    return render_template('index.html', news=db.data.find().limit(200))
@app.route('/news/<id>/')
def news_id(id):
    
    fact = db.analysis.find_one({"_id": ObjectId(id)})
    tonality = db.tonality.find_one({"_id": ObjectId(id)})
    print(tonality.get('tonality') )

    if fact is None:
        fact = 0
 
    return render_template('news.html', news = db.data.find_one({'_id': ObjectId(id)}), facts = fact.get('newsWithMention'), tonal = tonality.get('tonality') )

# @app.route('api/getNews/', methods=['GET'])
# def get_news():
#     if db.analysis.find_one({"_id": ObjectId(id)}) is None:
#         findFact(id)
#     return render_template('news.html', news = db.lolokj.find_one({'_id': ObjectId(id)}), fact = db.analysis.find_one({"_id": ObjectId(id)}))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)