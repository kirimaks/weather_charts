import os
from apscheduler.schedulers.background import BackgroundScheduler
from weather_charts.database import db_session, init_db
from weather_charts.models import Chart


def scraper_job():
    init_db()   # Create db if empty.

    chart_id = Chart.query.filter(Chart.chart_name == "The Black Sea temp")
    chart_id = chart_id.all()

    # Create sea chart if need.
    if not chart_id:
        chart = Chart(chart_name="The Black Sea temp")
        db_session.add(chart)
        db_session.commit()
        chart_id = chart.chart_id
    else:
        chart_id = chart_id[0].chart_id

    # Cmd with chart id argument.
    cmd = "cd weather_scraper; scrapy crawl pogoda -a chart_id={}".format(chart_id)

    os.system(cmd)


scheduler = BackgroundScheduler()
scheduler.add_job(scraper_job, "interval", minutes=15)

#scraper_job()
