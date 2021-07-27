from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from models import *

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
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()
#
# user = User(UserId='Mary1509',
#             HtmlUrl='https://github.com/Mary1509',
#             AvatarUrl='https://avatars.githubusercontent.com/u/54399719?v=4')
#
# issue = Issue(IssueId=944298296, HtmlUrl='https://github.com/Mary1509/Practice3/issues/3', Number=3,
#               Title='Third issue title', Body='Comment here')
#
# issueAction = IssueAction(UserId='Mary1509', ModifiedDate='2021-07-14 09:03:03')
# issueAction.Action = Action(ActionId='1', Title='opened')
# issue.Actions.append(issueAction)
#
# issueState = IssueState(ModifiedDate="2021-07-14 09:03:03")
# issueState.State = State(Title="open")
# issue.States.append(issueState)
#
# issueLabel = IssueLabel()
# issueLabel.Label = Label(Title="User story")
# issue.Labels.append(issueLabel)
#
# # user = addUser(opened)
# # print(user)
#
# session.add(issue)
# session.commit()
#


# with Session() as session:
#     # session.commit()
#     session.add(user)
#     session.commit()
# session.add(issue)
# session.commit()


# print(issue)
# print(issueLabel)
# print(issueState)
# print(issueAction)

# seeder = DatabaseSeeder()

# with Session() as session:
# session.add(user)
# session.add(issueState)
#     session.add(issue)
# session.add_all(seeder.users)
#
# session.add_all(seeder.issues)
# session.add_all(seeder.issueActions)
# session.add_all(seeder.actions)
#
# session.add_all(seeder.labels)
#
# session.add_all(seeder.states)

# session.add_all(seeder.issueLabels)
# session.add_all(seeder.issueStates)

# session.commit()
