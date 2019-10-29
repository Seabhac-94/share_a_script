import os
from flask import Flask, render_template, redirect, request, url_for
import pymongo
import dns
from flask_pymongo import PyMongo
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'share_a_script'
app.config['MONGO_URI'] = 'mongodb+srv://root:tqElhg634c6ax5@myfirstcluster-yibrd.mongodb.net/share_a_script?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def get_categories():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port= os.environ.get('PORT'),
    debug=True)