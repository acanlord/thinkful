from sqlalchemy import create_engine
from sqlalchemy.org import sessionmaker
from slalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


