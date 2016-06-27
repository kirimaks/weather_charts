from weather_charts import app
from flask_script import Manager
from celery import Celery

from jobs.scraper_job import scraper_job
import time

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

manager = Manager(app)


@celery.task
def scraper(n):
    while True:
        scraper_job()
        time.sleep(n)

scraper(10)

if __name__ == "__main__":
    manager.run()
