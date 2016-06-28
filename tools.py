from database.database import db_session
from app.models import Chart, DataSource
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def create_chart(chart_name):
    logger.debug("### Create chart [{}] ###".format(chart_name))

    chart = Chart(chart_name=chart_name)
    db_session.add(chart)
    db_session.commit()

    return chart.chart_id


def create_source(source_name):
    logger.debug("### Create source [{}] ###".format(source_name))

    source = DataSource(source_name=source_name)
    db_session.add(source)
    db_session.commit()
    return source.source_id
