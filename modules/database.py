from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

def connect_db():
    connection_string=os.environ.get('DATABASE_URL')
    db= create_engine(connection_string)
    Session=sessionmaker(bind=db)
    session=Session()
    return session

