from flask import render_template
from __init__ import app, COOKIE_TIME_OUT

from cruddy.app_crud import app_crud


app.register_blueprint(app_crud)
# create an instance of flask object


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")



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
