import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, text, Float

mod_dir = os.path.dirname(__file__)
basedir = str.join("/", mod_dir.split("/")[:-1])
sys.path.append(basedir)

from database.database import Base


class Chart(Base):
    __tablename__ = "charts"
    chart_id = Column(Integer, primary_key=True)
    chart_name = Column(String(256), nullable=False)

    def __repr__(self):
        return "[{}] {}".format(self.chart_id, self.chart_name)


class Data(Base):
    __tablename__ = "data"
    ref_id = Column(Integer, primary_key=True)
    indicator = Column(Float, nullable=False)
    time = Column(DateTime(timezone=True), server_default=text('now()'))

    chart_id = Column(Integer, ForeignKey("charts.chart_id"))
    source_id = Column(Integer, ForeignKey("sources.source_id"))

    def __repr__(self):
        return "indicator:({}) chart_id:[{}]".format(self.indicator,
                                                     self.chart_id)


class DataSource(Base):
    __tablename__ = "sources"
    source_id = Column(Integer, primary_key=True)
    source_name = Column(String(256), nullable=False)

    def __repr__(self):
        return "{}: {}".format(self.source_id, self.source_name)


def get_chart_data(source_id):
    data_offset = 30    # Last n rows from data table.
    buff = []
    for row in Data.query.filter(Data.source_id == source_id).order_by(Data.time).all()[-data_offset:]:
        time = row.time.timestamp() * 1000
        indicator = row.indicator
        buff.append([time, indicator])

    return buff
