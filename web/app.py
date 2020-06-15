from flask import Flask, request, render_template, json
from flask import jsonify, send_from_directory
from pymongo import MongoClient
import pymongo
import json
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def skiplimit(db, collection, page_size, page_num):
    """returns a set of documents belonging to page number `page_num`
    where size of each page is `page_size`.
    """
    # Calculate number of documents to skip
    skips = page_size * (page_num - 1)

    # Skip and limit
    cursor = db[collection].find().sort("_id", pymongo.DESCENDING).skip(skips).limit(page_size)

    # Return documents
    return [x for x in cursor]




@app.route('/')
def index():
    return render_template('index.html', news=db.data.find().sort("_id", pymongo.DESCENDING).limit(15))
@app.route('/news/<id>/')
def news_id(id):
    
    fact = db.analysis.find_one({"_id": ObjectId(id)}) 
    if fact is None:
        fact = 0
        tonality = 0 
    else: 
        tonality = db.tonality.find_one({"_id": ObjectId(id)}).get('tonality')
        fact =  fact.get('newsWithMention')

    return render_template('news.html', news = db.data.find_one({'_id': ObjectId(id)}), facts = fact, tonal = tonality )

@app.route('/facts/')
def facts():
    return render_template('facts.html', facts=db.analysis.find().limit(15))

@app.route('/w2v/')
def synonyms():
    return render_template('w2v.html')

@app.route('/api/getNews/<page_num>/', methods=['GET'])
def get_news(page_num):
    news = skiplimit(db,"data", 15,int(page_num))
    result = JSONEncoder().encode(news)
    return jsonify(result)

@app.route('/api/getFacts/<page_num>/', methods=['GET'])
def get_facts(page_num):
    news = skiplimit(db,"analysis",15,int(page_num))
    result = JSONEncoder().encode(news)
    return jsonify(result)

@app.route('/api/getSynm/<word>/', methods=['GET'])
def get_synm(word):

    return jsonify(db.synonyms.find_one({"word": word.lower()}).get('synom'))


# jsonify
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)