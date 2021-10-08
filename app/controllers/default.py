from app import app
from flask import render_template
from flask import session

@app.route("/")
def index():
    #session.clear()
    return render_template("index.html")