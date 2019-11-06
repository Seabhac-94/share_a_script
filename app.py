import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
import pymongo
import bcrypt
import dns
import env
from flask_pymongo import PyMongo
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
        login_user = users.find_one({'username' : request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('welcome_back'))
            else:
                flash("Incorrect username/password")
    return render_template('login.html')

"""
Welcome back page render
"""
@app.route('/welcome_back')
def welcome_back():
    return render_template('welcomeback.html')

"""
Register Users to Site
"""
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return render_template('welcome.html')
        else:
            flash("Username already taken!")    
    return render_template('signup.html')

"""
Logs Users Out of Site
"""
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))

"""
Brings users to share_a_script.html or login page depending on active session
"""
@app.route('/share_a_script')
def share_a_script():
    if 'username' in session:
        return render_template('share_a_script.html', categories=mongo.db.categories.find())
    else:
        return redirect(url_for('login'))

@app.route('/insert_script', methods=['POST'])
def insert_script():
        scripts = mongo.db.scripts
        author = mongo.db.authors
        existing_author = author.find_one({'first_name' : request.form['first_name'], 'last_name' : request.form['last_name']})
        if existing_author is None:
            author.insert_one({'first_name' : request.form['first_name'], 'last_name' : request.form['last_name']})
        scripts.insert_one(request.form.to_dict())
        return render_template('story_shared.html')

"""
Display categories.html
"""
@app.route('/get_categories')
def get_categories():
    categories=list(mongo.db.categories.find())
    return render_template('categories.html', categories=categories)

"""
Display Scripts in particular category
"""
@app.route('/view_scripts')
def view_scripts():
    scripts=list(mongo.db.scripts.find())
    return render_template('scripts.html', scripts=scripts)

@app.route('/get_authors')
def get_authors():
    authors=list(mongo.db.authors.find())
    return render_template('authors.html', authors=authors)

@app.route('/my_account')
def my_account():
    username = session["username"]
    scripts=list(mongo.db.scripts.find())
    return render_template('my_account.html', username=username, scripts=scripts)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port= os.environ.get('PORT'),
    debug=True)