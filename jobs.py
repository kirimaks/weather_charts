from apscheduler.schedulers.background import BackgroundScheduler
from weather_charts.database import db_session, init_db
from weather_charts.models import Chart, Data

from weather_scraper.scraper import get_water_temp


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

    temp = get_water_temp()

    data = Data(indicator=temp, chart_id=chart_id)

    db_session.add(data)
    db_session.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(scraper_job, "interval", minutes=10, max_instances=1)

# scraper_job()
