# __init__.py
from flask import Flask

# Setup of key Flask object (app)
app = Flask(__name__)

from flask_login import LoginManager

# The most important part of an application that uses Flask-Login is the LoginManager class.
# You should create one for your application like this:
# Setup LoginManager object (app)
login_manager = LoginManager()

# The login manager contains the code that lets your application and Flask-Login work together,
# such as how to load a user from an ID,  where to send users when they need to log in, and the like.
# Once the actual application object has been created, you can configure it for login with:

login_manager.init_app(app)


# model.py
# The class that you use to represent users needs to implement these properties and methods:
# is_authenticated, is_active, is_anonymous, get_id()
# To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations
# for all of these properties and methods.

from flask_login import UserMixin
# Users DB is a collection Data Structure
class Users(UserMixin, db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes instance variables within object
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.set_password(password) #encrypt password
        self.phone = phone

# required for login_user, overrides id (login_user default) to implemented userID
# The method get_id() must return a str that uniquely identifies this user, and can be used to load the user
# from the user_loader callback.
def get_id(self):
    return self.userID


from werkzeug.security import generate_password_hash, check_password_hash

# set password method is used to create encrypted password
def set_password(self, password):
    """Create hashed password."""
    * Procedural Abstraction
    self.password = generate_password_hash(password, method='sha256')

# check password to check versus encrypted password
def is_password_match(self, password):
    """Check hashed password."""
    result = check_password_hash(self.password, password)
    return result


# query.py

from __init__ import login_manager, db
from cruddy.model import Users
from flask_login import current_user, login_user, logout_user

# login user based off of email and password
def login(email, password):
    # sequence of checks
    if current_user.is_authenticated:  # return true if user is currently logged in
        return True
    elif is_user(email, password):  # return true if email and password match
        user_row = user_by_email(email)
        login_user(user_row)  # sets flask login_user
        return True
    else:  # default condition is any failure
        return False


# this function is needed for Flask-Login to work.
# User_loader callback. This callback is used to reload the user object from the user ID stored in the session.
# It should take the str ID of a user, and return the corresponding user object.
# It should return None (not raise an exception) if the ID is not valid.

@login_manager.user_loader
def user_loader(user_id):
    """Check if user login status on each page protected by @login_required."""
    if user_id is not None:
        return Users.query.get(user_id)
    return None


# Authorize new user requires user_name, email, password
def authorize(name, email, password):
    if is_user(email, password):
        return False   #email already exist in DB
    else:
        # auth_user is an object of class Users
        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone="1234567890"  # this should be added to authorize.html Hack #1
        )
        # Password is encrypted in the init method of the class with self.set_password(password)
        # Add it to the auth_user object
        auth_user.create()
        return True


# logout user
Hack #2 Add logout to CRUD screen
def logout():
    logout_user()  # removes login state of user from session