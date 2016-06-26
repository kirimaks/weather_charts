from weather_charts import app
from flask import render_template
from weather_charts.models import Data


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/table")
def about():
    data_rows = Data.query.all()
    return render_template("table.html", data_rows=data_rows)
