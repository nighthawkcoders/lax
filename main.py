from flask import render_template, redirect, request, url_for
from flask_login import login_required
from __init__ import app, login_manager

from cruddy.app_crud import app_crud
from homepages.homepages import app_homepages
from app_notes import app_notes
from uploady.app_upload import app_upload



app.register_blueprint(app_upload)
app.register_blueprint(app_crud)
app.register_blueprint(app_homepages)
app.register_blueprint(app_notes)
# create an instance of flask object

# serve uploaded files so they can be downloaded by users.
@app.route('/<name>')
def uploads_endpoint(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


# register "uploads_endpoint" endpoint so url_for will find all uploaded files
app.add_url_rule(
    "/" + app.config['UPLOAD_FOLDER'] + "/<name>", endpoint="uploads_endpoint", build_only=True
)

# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")

@app.route('/signup/')
def signup():
    return render_template("signup.html")


@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/wallOfFame/')
def wallOfFame():
    return render_template("awards/wallOfFame.html")

@app.route('/alumni/')
def alumni():
    return render_template("awards/alumni.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/roster/")
def roster():
    return render_template("roster.html")


# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(
        host='127.0.0.1',
	    debug=True,
	    port=8080
    )
