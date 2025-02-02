from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/db_bank')

sessionLocal = sessionmaker(bind=engine)