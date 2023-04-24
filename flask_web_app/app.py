from bson.objectid import ObjectId
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from urllib.parse import quote_plus
import os


#mongo = os.getenv('MONGO')
username= os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'bibi')
password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', '029365947')
mongo_host = os.environ.get('MONGO', 'localhost')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))
myclient = MongoClient(host=[f"{mongo_host}:{mongodb_port}"], username=username, password=password)
#myclient = MongoClient(username=username, password=password)
#myclient = MongoClient(host=[f"{mongo_host}:{mongodb_port}"])
#host = f"{mongo}:27017"
#uri = "mongodb://%s:%s@%s" % (quote_plus(username), quote_plus(password), host)
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#client = MongoClient(mongo, 27017,username, password)
#client = MongoClient(uri)
#client = MongoClient('localhost', 27017, username='bibi', password='029365947')
print(f"my mongo client: {myclient}")
print(f"u p: {username}: {password}")
db = myclient.flask_db
todos = db.todos


app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8088)