Currently under progress.

# Share a Script

Share a Script is a project done under the requirements for MS3 Project - Data-Centric-Development w/Code Institute.
<br>
The idea for Share a Script was orignally conceived in June 2019. The intention of this site is to provide up-and-coming writers with a platform to share their work and have it critiqued by other authors.
#

## UX

#### Design Considerations
1. Background: A stack of books. Simple, yet to the point. This particular photo was chosen for it's classic approach to books.
2. Icons - Three main icons have been chosen for this site, a feather, scroll, and home, each clearly identifying the purpose, of writing, reading and returning to the home page. Simple and easy to understand.
3. 

#

## Features

The following features have been implemented already:

#### Existing Features
1. User Registration: User's who wish to submit their work to the site will have to register first. This is done using Flask, Bcrypt and MongoDB as the database for users.
2. User Login: As above. Registered users must login before attempting to share work on the site.
3. Flash messages indicating if Username is already taken at registration, or incorrect username/password at login.
4. User Logout: Enables the user to end the session.
5. Navbars: The navbars are designed to change depending on whether or not users are logged in or not.
6. Share Your Story: Once users are logged in they will have access to the Share Your Story form. This form will give the user an option of inputing Author's First and Last Name - this part of the form in particular is important as it gives the user an option of giving a psuedo-name or "Anonymous".
7. Delete Script: Users have the ability to delete scripts that only they have shared from the My Account section


#### Possible Future Features 
1. Comments section: Give other users the ability to comment/critique on others work.

#
## Technologies/Frameworks Used
1. HTML5 
2. CSS3
3. JavaScript
4. <a href='https://www.python.org/'>Python</a>
5. <a href='https://www.mongodb.com/'>MongoDB</a>
6. <a href='https://flask.palletsprojects.com/en/1.1.x/'>Flask</a>
6. <a href='https://pypi.org/project/bcrypt/'>Bcrypt</a>
7. <a href='https://getbootstrap.com/'>Bootstrap</a>
8. <a href='https://fontawesome.com/'>Font Awesome</a>

#
## Testing
This site was developed through constant testing of functionality. The below tests are a record of the process from initial code, to testing, debugging, to retesting.

##### Initialising the app.
1. Initialise the app.route('/') and app.route('/index') and return "Hello World!". Ensure "if __name__ == '__main__' " is configured with debug=True. 
2. Run the app.py file and open the browser - Hello World! is there, app is running.

##### Conecting to MongoDB
1. Set up the env file with the secret_key and MONGO_URI and add to .gitignore.
2. Import env into app.py.
3. On MongoDB Atlas, create some data for author names in a new collection to be displayed.
4. Create the @app.route('/get_authors') and set it to return render_template('authors.html' authors=mongo.db.authors.find()).
5. In authors.html create a small loop in a list object to iterate through the authors.
6. Open the authors.html - list of authors is displaying correctly. App is connected to MongoDB.

##### Creating a User Registration
1. After writing initial code for registering users, create a simple form for registration - username and password are only required for now.
2. Attempt to register user, if site redirects to index as expected after a successful registration, head to MongoDB and check the user collection.
3. User is in the collection, with username and an encrypted password - initial test passed.
4. Add more fields to the form, first name, last name, and repeat the tests.
5. Having multiple user's with the same username is not an option - so "if exisiting_user is None" a return "Username already taken" should appear.
6. Test this functionality by attempting to register with the same username as before - return message should show.
7. Once this has passed a flash message is configured.
8. Repeat the test, this time a message should appear above the username field with the message "Username already taken"
9. All tests passed.

##### Creating a User Login
1. After writing initial code for user, create a simple form for login - username and password are only required.
2. It was initially found that the login.html page wouldn't render due to a method issue. Upon further trouble shooting, the code was found to have 2 major issues - incorrect method was being used for submitting the form, and a 'return redirect('login.html') ' was being used, instead of 'return render_template('login.html')' - this caused an issue as the site was trying to redirect to a page that hadn;t yet been rendered.
3. The login page is now rendering so a basic login test was done using a username and password used to register - the test failed with a "AttributeError: 'bytes' object has no attribute 'encode' " - further research was done on the Bcrypt module, and it was found that there was 2 .encode(utf-8) inserted where they shouldn't have been. The code being used to compare the passwords was of an older version and had since been updated.
4. The test was repeated and passed. Once the user had logged in successfully, they were redirected to index. Later this was updated so that the user was redirected to a welcome page.

##### Sharing a Script

##### Deleting a Script




##### Testing Procedure for Responsiveness

#
## Deployment

- what needs to be installed
- how to create requirements.txt and Procfile,
- how to create a new app on heroku
- How to push to heroku or link to guthub depending on which method you used.
- How to set config vars on heroku
- Final steps you took to deploy it.

#
## Credits

#### Sources

#### Media

Background Image - https://www.enigma-mag.com/5-books-to-read-this-month/stack-of-books-great-education/
