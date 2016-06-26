from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, text
from weather_charts.database import Base


class Chart(Base):
    __tablename__ = "charts"
    chart_id = Column(Integer, primary_key=True)
    chart_name = Column(String(256), nullable=False)

    def __repr__(self):
        return "[{}] {}".format(self.chart_id, self.chart_name)


class Data(Base):
    __tablename__ = "data"
    ref_id = Column(Integer, primary_key=True)
    indicator = Column(Integer, nullable=False)
    chart_id = Column(Integer, ForeignKey("charts.chart_id"))
    time = Column(DateTime(timezone=True), server_default=text('NOW()'))

    def __repr__(self):
        return "indicator:({}) chart_id:[{}]".format(self.indicator,
                                                     self.chart_id)
