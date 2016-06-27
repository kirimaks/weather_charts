import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mod_dir = os.path.dirname(os.path.abspath(__file__))
basedir = str.join("/", mod_dir.split("/")[:-1])
sys.path.append(basedir)

engine = create_engine("postgresql://dfcxhwvghrjcut:ADw_Vg6BtHPuxdhaq_7jPGRgfX@ec2-176-34-103-75.eu-west-1.compute.amazonaws.com/d94bmnricksn05", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.models
    Base.metadata.create_all(bind=engine)
