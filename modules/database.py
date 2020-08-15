from sqlalchemy import create_engine

def connect_db():
    connection_string="postgresql://postgres:7538821247@localhost:5432/shopping"
    return create_engine(connection_string)

