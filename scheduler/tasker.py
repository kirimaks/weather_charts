from apscheduler.schedulers.background import BackgroundScheduler
import socket

import logging
from scheduler.tasks import yandex_temp, sochicamera_temp, worldseatemp_temp
from scheduler.tasks import wake_up

logging.basicConfig(level=logging.DEBUG)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 47200))
except socket.error:
    logging.debug("Already started, skipping...")
else:
    scheduler = BackgroundScheduler()

    scheduler.add_job(wake_up, "interval", minutes=25)

    scheduler.add_job(yandex_temp, "interval", hours=6)
    scheduler.add_job(sochicamera_temp, "interval", hours=6)
    scheduler.add_job(worldseatemp_temp, "interval", hours=6)

    scheduler.start()
    logging.debug("<< Scheduler started >>")
