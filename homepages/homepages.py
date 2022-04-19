import requests
from flask import Blueprint, render_template, request

app_homepages = Blueprint('homepages', __name__,
                          url_prefix='/homepages/',
                          template_folder='templates/homepages/',
                          static_folder='static',
                          static_url_path='static/assets')


@app_homepages.route('/aboutAllison/')
def aboutArch():
    return render_template("aboutAllison.html")

@app_homepages.route('/aboutBria/')
def connor_homepage():
    return render_template("aboutBria.html")

@app_homepages.route('/aboutChristina/')
def davidhomepage():
    return render_template("aboutChristina.html")

@app_homepages.route('/aboutDavid/')
def derrickpage():
    return render_template("aboutDavid.html")

@app_homepages.route('/aboutKaavya/')
def reinhardtpage():
    return render_template("aboutKaavya.html")
