# EXPRESSO: Fuel Your Thoughts : BOLD, STRONG AND UNFILTERED
#### Video Demo:  <https://youtu.be/oB2fwCkjmPM>
#### Description:

Hey Everyone! Madhav Here From Delhi, India. I am currently pursuing B.Tech. in Electronics Field From MAIT, DELHI.
Today , I wanna introduce you to EXPRESSO. It is basically a social media app where you can post your thoughts and get views about your post from the public. In this way you can connect with the world out there.

Tech Stack Used: Python, SQL (Embedded in Python), HTML, CSS, Javascript, Flask, Jquery, Bulma CSS Library, Jinja Templating Engine

So now, let me show you , how this was made:-
1. instance/ : This folder contains the session data in the form of a database.db file.
    in database.db: I had 4 models/tables : Post, Like, Comment, User

2. Website/static/ : This contains the common css of all the html files , the images used in the design (like-icon,    brand icon, post-icon), the common javascript file for all html files.

3. Website/templates/ : This contains all the templates or the html files . The logic in these files is met by The Jinja Templating Engine. Let us take a brief look at all of them :-
    1. about.html : This contains the html for "about" page. The content is passed in from the corresponding view route from views.py.
    2. contact.html : This contains the html for "contact-us" page. The content is passed in from the corresponding view route from views.py.
    3. post_layout.html : This contains the post_layout of the card containing the post . It also houses the logic for different features like comment, like, like-icon etc. Here, the like-icon is implemented in index.js file.
    4. layout.html : This is the common page of all of the templates to avoid repitition of the same code tens of times. This file is included or extended to all of the files through jinja command of {% extends "name_of_the_file.html" %}
    5. index.html : This is the home page containing all posts. The post_layout template is extended to it for each post. Each post is accessed through the for loop. Here, the navbar-collapse is implemented in index.js file.
    6. login.html : This is the login page containing some welcome remarks , and some inputs for login details along with a login button. It verifies whether a user has registered or not.
    7. register.html : Template for registering a user . Contains some new user remarks and some inputs for registering a user. It contains the major checks for registering a user like username, password, email too short, confirm password to let user verify their password. It also checks whether the email or username already exists. The password is hashed before it's saved to ensure privacy.
    8. posts.html : Through this template you can access the posts of a certain user by clicking on their username.

4. Website/__init__.py : For initializing app , User and the Database.

5. Website/auth.py : For authorizing the user while Logging In, Signing Up and Logging Out. Contains all the checks of the user credentials.

6. Website/models.py : Contains the template of the models/tables. There are 4 models used : User, Post, Comment, Like.

7. Website/views.py : Handles the rendering of all templates except login and register. This is the longest file in this whole project. It contains all the view routes for handling each route properly.

8. Project/app.py : For initializing the app.

Dependencies of Flask:-
1. flask_login
2. LoginManager
3. flask_sqlalchemy
4. os
5. flask
6. werkzeug.security

# To Run This , import the folder into your local workspace and run "python app.py" command in terminal. Go to the server port to experience my creation. Make sure you had installed all dependencies mentioned in this file.


This is basically my first web app which I am uploading on github. 
Hope You'll Like It.