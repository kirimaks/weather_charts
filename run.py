from weather_charts import app, current_app
from flask_script import Manager

from jobs.scraper_job import scraper_job
import time
import threading


def run_job(n):
    while True:
        scraper_job()
        time.sleep(n)


manager = Manager(app)

with app.app_context():
    current_app.threadLock = threading.Lock()

    if not current_app.threadLock.locked():
        current_app.threadLock.acquire()
        run_job(60)
    else:
        print("Passing")


if __name__ == "__main__":
    manager.run()
