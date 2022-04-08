from flask import Flask

app = Flask(__name__)

from flask_login import LoginManager


login_manager = LoginManager()

# To make implementing a user class easier, you can inherit - KC
login_manager.init_app(app)


from flask_login import UserMixin

class Users(UserMixin, db.Model):
    # following data-model property names are fixed: - KC
    # SQLAlchemy allows developers to specify a database column name different - KC
    # from their corresponding data-model property name - KC
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)
# Python, def_init_(self): syntax error - KC
#     There should always be a colon at the end of a function definition (followed by the body of the function). - KC
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.set_password(password) #encrypt password
        self.phone = phone


def get_id(self):
    return self.userID


from werkzeug.security import generate_password_hash, check_password_hash


def set_password(self, password):
    """Create hashed password."""
    * Procedural Abstraction
    self.password = generate_password_hash(password, method='sha256')


def is_password_match(self, password):
    """Check hashed password."""
    result = check_password_hash(self.password, password)
    return result

# This will bind the Flask-Login to the server. However, this does not seem to have any effect.

# Need to find the URL of the landing

# This does not have a default login URL in the Flask-Login, so we need to specify

from __init__ import login_manager
from model import Users
from flask_login import current_user, login_user, logout_user

def login(email, password):

    if current_user.is_authenticated:
        return True
    elif is_user(email, password):
        user_row = user_by_email(email)
        login_user(user_row)
        return True
    else:
        return False



@login_manager.user_loader
def user_loader(user_id):
    if user_id is not None:
        return Users.query.get(user_id)
    return None


def authorize(name, email, password):
    if is_user(email, password):
        return False
    else:

        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone="1234567890"
        )

        auth_user.create()
        return True


Hack
def logout():
    logout_user()
