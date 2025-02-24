import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:password@db:5432/case_gol', echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
Base.metadata.create_all(bind=engine, checkfirst=True)