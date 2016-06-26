import sys
import os.path

from apscheduler.schedulers.background import BackgroundScheduler
from weather_charts.database import db_session, init_db
from weather_charts.models import Chart

# Add scrapy project path.
mod_path = os.path.abspath(__file__)
scrapy_dir = os.path.dirname(mod_path) + "/weather_scraper"
sys.path.append(scrapy_dir)

# scrapy
from scrapy.crawler import CrawlerProcess
from weather_scraper.spiders.pogoda import PogodaSpider
from weather_scraper import settings


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

    # Generate settings.
    settings_dict = {k: settings.__dict__[k]
                     for k in dir(settings) if not k.startswith("__")}

    process = CrawlerProcess(settings_dict)
    process.crawl(PogodaSpider, chart_id=chart_id)
    process.start()


scheduler = BackgroundScheduler()
scheduler.add_job(scraper_job, "interval", minutes=10, max_instances=1)

# scraper_job()
