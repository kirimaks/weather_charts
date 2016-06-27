from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.scraper_job import scraper_job
import socket

from run import logging


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 47200))
except socket.error:
    logging.debug("Already started, skipping...")
else:
    scheduler = BackgroundScheduler()
    scheduler.add_job(scraper_job, "interval", minutes=1)
    scheduler.start()
    logging.debug("-- Scheduler started --")
