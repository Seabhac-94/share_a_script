import os
from flask import (Flask, render_template, 
redirect, request, url_for, session, flash, Markup)
import pymongo
import bcrypt
import dns
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
Brings users to share_a_script.html or login page depending on active session
"""
@app.route('/share_a_script')
def share_a_script():
    categories=mongo.db.categories.find()
    if 'username' in session:
        username = session["username"]
        return render_template('share_a_script.html', 
        categories=categories, username=username)
    else:
        return redirect(url_for('login'))

"""
User Login
"""
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), 
                            login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('welcome'))
            flash("Incorrect username/password")
        flash("Incorrect username/password")
    return render_template('login.html')

"""
Welcome back page render
"""
@app.route('/welcome')
def welcome():
    username = session["username"]
    return render_template('welcome.html', username=username)

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
            users.insert_one({'first_name' : request.form['first_name'], 
                                'last_name' : request.form['last_name'], 
                                'username' : request.form['username'],
                                'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
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
Allows users to share a script
"""
@app.route('/insert_script', methods=['POST'])
def insert_script():
        scripts = mongo.db.scripts
        author = mongo.db.authors
        existing_author = author.find_one({'author_name' : request.form['author_name']})
        if existing_author is None:
            author.insert_one({'author_name' : request.form['author_name']})
        scripts.insert_one(request.form.to_dict())
        return render_template('story_shared.html')


"""
Display Scripts in particular category
"""

@app.route('/view_scripts')
def view_scripts():
    categories = list(mongo.db.categories.find())
    scripts=list(mongo.db.scripts.find())
    titles=list(mongo.db.titles.find())
    return render_template('scripts.html', scripts=scripts, 
                            categories=categories, titles=titles)
    
"""
Personalised account for user
"""
@app.route('/my_account')
def my_account():
    username = session["username"]
    scripts=list(mongo.db.scripts.find())
    return render_template('my_account.html', 
                            username=username, 
                            scripts=scripts)

"""
Delete a script from my_account
"""
@app.route('/delete_script/<script_id>')
def delete_script(script_id):
    mongo.db.scripts.remove({'_id': ObjectId(script_id)})
    return redirect(url_for('my_account'))

"""
Edit a script from my_account
"""

@app.route('/update_script/<script_id>', methods=['POST'])
def update_script(script_id):
    script = mongo.db.scripts
    script.update( {'_id': ObjectId(script_id)},
    {   'author_name':request.form.get('author_name'),
        'uploaded_by':request.form.get('uploaded_by'),
        'title':request.form.get('title'),
        'chapter_name': request.form.get('chapter_name'),
        'category_name': request.form.get('category_name'),
        'script': request.form.get('script')
    })
    return redirect(url_for('my_account'))


@app.route('/edit_script/<script_id>')
def edit_script(script_id):
    username = session["username"]
    script =  mongo.db.scripts.find_one({"_id": ObjectId(script_id)})
    categories =  mongo.db.categories.find()
    return render_template('edit_script.html', script=script, 
                            categories=categories, username=username)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port= os.environ.get('PORT'),
    debug=False)