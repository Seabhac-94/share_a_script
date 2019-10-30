import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
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




"""
App opens on home page
"""
@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template('index.html')



@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', categories=mongo.db.categories.find())

@app.route('/get_authors')
def get_authors():
    return render_template('authors.html', authors=mongo.db.authors.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port= os.environ.get('PORT'),
    debug=True)