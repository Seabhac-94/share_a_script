# Share a Script

Share a Script is a project done under the requirements for MS3 Project - Data-Centric-Development w/Code Institute.
<br>
The idea for Share a Script was orignally conceived in June 2019. The intention of this site is to provide up-and-coming writers with a platform to share their work and have it critiqued by other authors.
#
Deployed App: <a target="_blank" href = "https://share-a-script.herokuapp.com/">Share a Script</a>

Login with: 
username = default_user
<br>
password = default_password
<br>
to access full functionality, or feel free to <a target="_blank" href="https://share-a-script.herokuapp.com/register">Sign-Up</a> yourself!

Github Repo: <a target="_blank" href="https://github.com/Seabhac-94/share_a_script">share_a_script</a>

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
7. My Account - Users can see their own individual scripts rom the My Account section.
8. Delete Script: Users have the ability to delete scripts that only they have shared from the My Account section
9. Edit Script: Users have the ability to edit scripts that only they have shared from the My Account section
10. View scripts: Any visitiors to the site can view all work on the site, sorted by category.


#### Possible Future Features 
1. Comments section: Give other users the ability to comment/critique on others work.

#
## Technologies/Frameworks Used
1. HTML5 
2. CSS3
3. JavaScript
4. <a target="_blank" href='https://www.python.org/'>Python</a>
5. <a target="_blank" href='https://www.mongodb.com/'>MongoDB</a>
6. <a target="_blank" href='https://flask.palletsprojects.com/en/1.1.x/'>Flask</a>
6. <a target="_blank" href='https://pypi.org/project/bcrypt/'>Bcrypt</a>
7. <a target="_blank" href='https://getbootstrap.com/'>Bootstrap</a>
8. <a target="_blank" href='https://fontawesome.com/'>Font Awesome</a>

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
1. After writing initial code in app.py and creating the form, try to submit a simple script with all inputs as 'Test'. Check the MongoDB for the 'Test'
2. The 'Test' does upload, however, initially there is no way of regulating the form - ie. required fields, and attachment to a user.
3. Insert 'required' into each form-group and attempt to submit the form while leaving one form-field blank at a time - popup appears.
4. Create another field as 'uploaded_by' with 'readonly' attribute and input the username in session as value - this will attach the script to the user while also not allowing the user to edit the field.
5. Run the same "Test" again with all fields correctly filled, and check MongoDB - script has uploaded correctly.


##### Deleting a Script
1. Create a remove function in app.py and link it to my_account.html.
2. Attempt to delete "Test" from previous tests.
3. No issues - "Test" is deleted from MongoDB.

##### Editing a Script
1. After creating form and function - click on the 'Edit' from My Account and attempt to edit script.
2. Initially only First Name, Last Name, Title, Chapter Name and Script were available for editing, this resulted in category_name, and uploaded_by being removed when editing was done.
3. category_name and uploaded_by were insterted into the form again, and the values of each form group were changed to match the original values, this gives the user a better editing experience.
4. Attempt to edit "Test" , change each field and submit.
5. Succesfully edited and visible in My Account, View Scripts and MongoDB.


##### Testing Procedure for Responsiveness

1. Developer tools was opened and the above tests were completed on a number of different platforms including iPhone 5/SE, iPhone 6/7/8, iPAd, iPad Pro, iPad Mini, Galaxy S5, Pixel 2, Pixel 2XL. Along with this, standard settings form the size bar were selcted, i.e; Mobile S/M/L, Tablet, Laptop & Laptop L.
2. For each device, the site was checked to enure there was no overlap of information and that the presentation looked well.

#
## Deployment

#### Modules to be installed
1. os
2. Flask - render_template, redirect, request, url_for, session, flash
3. PyMongo
4. flask_pymongo
4. Bcrypt
5. bson.objectid - ObjectId 

#### Creating a requirements.txt and Procfile

1. In CLI input pip3 freeze --local > requirements.txt . This should generate a file with all tools listed and they're version number.
2. Procfile - in CLI input echo web: python app.py > Procfile

#### Creating an app on Heroku
1. Create account with Heroku.
2. Select "New" then "Create new app"
3. Input app-name and region (Europe in this case)
4. Follow steps for "Deploy using Heroku Git" (push from CLI, described below)
5. Set Config vars (described below)

##### Push to Heroku
1. First, ensure requirements.txt and Procfile are configured.
2. In temrinal window, run "heroku login"
3. Press and key to be redirected to Heroku Login page, select "Login in to Heroku CLI"
4. Return back to Terminal, Herok ushould be logged in, run the command "git push heroku master".
5. Once successfully completed, " https://share-a-script.herokuapp.com/ deployed to Heroku" will be available in terminal window, you can follow this link to view your application.

##### Set config vars on Heroku
1. From your app dashboard, select settings.
2. In settings, select "Reveal config vars"
3. The following need to be configured;

- I.P  : 0.0.0.0
- PORT : 5000
- MONGO_URI : mongodb+srv://root:password@clustername-yibrd.mongodb.net/collectionname?retryWrites=true&w=majority
- SECRET_KEY : secret_key

##### Final steps
1. Ensure Debug is set to False in app.py
2. Removed import env form app.py, the config vars are set through Heroku, env.py is just for development purposes only.

#
## Credits

#### Sources

With the exception of 'Goodbye, Old Friend' and 'I Don't Understand', all scripts were taken from <a target="_blank" href="https://www.bookscool.com/en/index.php">Bookscool</a> and <a target="_blank" href="https://zelalemkibret.files.wordpress.com/2012/01/the-autobiography-of-nelson-mandela.pdf">Long Walk to Freedom</a> to only populate the data - the intention is to remove these once the site is populated with new artists' work.


#### Media

Background Image - <a target="_blank" href="https://www.enigma-mag.com/5-books-to-read-this-month/stack-of-books-great-education/">Enigma</a>