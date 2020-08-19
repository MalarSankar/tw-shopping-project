from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_db():
    connection_string="postgresql://postgres:7538821247@localhost:5432/shopping"
    db= create_engine(connection_string)
    Session=sessionmaker(bind=db)
    session=Session()
    return session

