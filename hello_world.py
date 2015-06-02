from bottle import route, run, template
from pymongo import MongoClient

@route('/')
def index():
    connection = MongoClient('localhost', 27017)
    db = connection.test
    item = db.names.find_one()
    return template('<b>Hello {{name}}</b>!', name=item['name'])

run(host='localhost', port=8080)



