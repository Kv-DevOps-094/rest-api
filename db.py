from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models import *
# from seeder import DatabaseSeeder

DATABASE = "issuedb"
USER = "postgres"
PASSWORD = "Init1234"
HOST = "localhost"
PORT = "5432"

db_url = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Create db
if not database_exists(db_url):
    create_database(db_url)

# Create tables
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)

# Create session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# seeder = DatabaseSeeder()

# with Session() as session:
#     session.add_all(seeder.users)
#     session.add_all(seeder.issues)
#     session.add_all(seeder.labels)
#     session.add_all(seeder.issueLabels)
#     session.add_all(seeder.actions)
#     session.add_all(seeder.issueActions)
#     session.add_all(seeder.states)
#     session.add_all(seeder.issueStates)
#     session.commit()
