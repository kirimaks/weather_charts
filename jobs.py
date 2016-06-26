from apscheduler.schedulers.background import BackgroundScheduler

from weather_charts.database import db_session, init_db
from weather_charts.models import Data, Chart
from random import randrange


def scraper_job():
    init_db()   # Create db if empty.

    chart_id = Chart.query.filter(Chart.chart_name == "The Black Sea temp").all()
    if not chart_id:
        chart = Chart(chart_name="The Black Sea temp")
        db_session.add(chart)
        db_session.commit()
        chart_id = chart.chart_id
    else:
        chart_id = chart_id[0].chart_id

    num = randrange(1, 100)

    print("Chart_id:[{}], {}".format(chart_id, num))

    data = Data(indicator=num, chart_id=chart_id)
    db_session.add(data)
    db_session.commit()


scheduler = BackgroundScheduler()
scheduler.add_job(scraper_job, "interval", minutes=1)
