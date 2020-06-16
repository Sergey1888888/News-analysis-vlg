from run import create_w2v_model
from dbtext import newsToText

client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
db = client.news

newsToText(db.data)
create_w2v_model()
