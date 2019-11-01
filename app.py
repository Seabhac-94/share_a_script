import os
from flask import Flask, render_template, redirect, request, url_for, session
import pymongo
import bcrypt
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
@app.route('/index')
def index():
    return render_template('index.html')

"""
User Login
"""


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
    else:
        return render_template('login.html')


"""
Register Users to Site
"""
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('signup.html')

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