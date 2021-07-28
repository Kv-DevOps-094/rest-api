from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from models import *

DATABASE = "issuedb"
USER = "postgres"
PASSWORD = "Init1234"
HOST = "localhost"
PORT = "5432"

db_url = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Create db
# drop_database(db_url)
if not database_exists(db_url):
    create_database(db_url)

# Create tables
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)

db_session = sessionmaker(bind=engine)

