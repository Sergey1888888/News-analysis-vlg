from flask import Flask, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
sys.path.append("../tomita")
from tomita import findFact
import datetime
app = Flask(__name__)
client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news

@app.route('/')
def index():
    return render_template('index.html', news=db.lolokj.find().limit(200))
@app.route('/news/<id>/')
def news_id(id):
    if db.analysis.find_one({"_id": ObjectId(id)}) is None:
        findFact(id)
    return render_template('news.html', news = db.lolokj.find_one({'_id': ObjectId(id)}), fact = db.analysis.find_one({"_id": ObjectId(id)}))

if __name__ == "__main__":
    app.run(debug=True)