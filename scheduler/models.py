from sqlalchemy import Column, Integer, DateTime, text
from database.database import Base


class Scheduler(Base):
    __tablename__ = "scheduler"
    job_id = Column(Integer, primary_key=True)
    start_time = Column(DateTime(timezone=True), server_default=text('NOW()'))
