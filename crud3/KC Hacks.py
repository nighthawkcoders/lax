from flask import Flask

app = Flask(__name__)

from flask_login import LoginManager


login_manager = LoginManager()


login_manager.init_app(app)


from flask_login import UserMixin

class Users(UserMixin, db.Model):

    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

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
    """Check if user login status on each page protected by @login_required."""
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