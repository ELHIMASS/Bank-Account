
from flask import Flask
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

Base = declarative_base()
Base1 = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:@localhost/db_bank')

sessionLocal = sessionmaker(bind=engine)
