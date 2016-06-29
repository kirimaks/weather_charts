from app import application
from flask import render_template
from app.models import Data, get_chart_data


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/table")
def about():
    data_rows = Data.query.all()
    return render_template("table.html", data_rows=data_rows)


@application.route("/charts")
def charts():

    worldseatemp_data = get_chart_data(source_id=1)
    yandex_data = get_chart_data(source_id=2)
    sochicamera_data = get_chart_data(source_id=3)

    return render_template("charts.html",
                           worldseatemp_data=worldseatemp_data,
                           yandex_data=yandex_data,
                           sochicamera_data=sochicamera_data)
