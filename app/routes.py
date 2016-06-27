from app import application
from flask import render_template
from app.models import Data


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/table")
def about():
    data_rows = Data.query.all()
    return render_template("table.html", data_rows=data_rows)
