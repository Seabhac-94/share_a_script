import os
from flask import Flask, render_template, redirect, request, url_for
import pymongo
import dns
from flask_pymongo import PyMongo
import env
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config["MONGO_DBNAME"] = "share_a_script"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def get_categories():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port= os.environ.get('PORT'),
    debug=True)