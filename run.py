from weather_charts import app
from flask_script import Manager

from jobs.scraper_job import scraper_job
import time


def run_job(n):
    while True:
        scraper_job()
        time.sleep(n)


manager = Manager(app)

with app.app_context():
    run_job(60)


if __name__ == "__main__":
    manager.run()
