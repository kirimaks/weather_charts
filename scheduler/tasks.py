from database.database import db_session, init_db
from app.models import Chart, Data, DataSource
import logging

from scrapers.yandex import get_temp_yandex
from scrapers.sochicamera import get_temp_sochicamera
from scrapers.worldseatemp import get_temp_worldseatemp
from tools import create_source, create_chart
import requests

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)

init_db()   # Create db if empty.
chart_name = "The Black Sea temp"
chart_id = Chart.query.filter(Chart.chart_name == chart_name)
chart_id = chart_id.all()

# Create sea chart if need.
if not chart_id:
    chart_id = create_chart(chart_name)
else:
    chart_id = chart_id[0].chart_id


def yandex_temp():
    logging.debug("yandex_temp() started")

    source_name = "yandex"

    source_id = DataSource.query.filter(DataSource.source_name == source_name)
    source_id = source_id.all()

    if not source_id:
        source_id = create_source(source_name)
    else:
        source_id = source_id[0].source_id

    temp = get_temp_yandex()
    data = Data(indicator=temp, chart_id=chart_id, source_id=source_id)

    db_session.add(data)
    db_session.commit()


def sochicamera_temp():
    logging.debug("sochicamera_temp() started")
    source_name = "sochicamera"

    source_id = DataSource.query.filter(DataSource.source_name == source_name)
    source_id = source_id.all()

    if not source_id:
        source_id = create_source(source_name)
    else:
        source_id = source_id[0].source_id

    temp = get_temp_sochicamera()

    data = Data(indicator=temp, chart_id=chart_id, source_id=source_id)

    db_session.add(data)
    db_session.commit()


def worldseatemp_temp():
    logging.debug("worldseatemp_temp() started")
    source_name = "worldseatemp"

    source_id = DataSource.query.filter(DataSource.source_name == source_name)
    source_id = source_id.all()

    if not source_id:
        source_id = create_source(source_name)
    else:
        source_id = source_id[0].source_id

    temp = get_temp_worldseatemp()

    data = Data(indicator=temp, chart_id=chart_id, source_id=source_id)

    db_session.add(data)
    db_session.commit()


def wake_up():
    logging.debug("WakeUp() started")
    resp = requests.get("https://weather-graphs.herokuapp.com/table")
    logging.debug("Done, code: [{}]".format(resp.status_code))
