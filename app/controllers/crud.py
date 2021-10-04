from app import app
from flask import render_template

@app.route("/crud")
def crud():
    return render_template("crud.html")