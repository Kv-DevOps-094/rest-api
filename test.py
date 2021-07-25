import json
from types import SimpleNamespace
from sqlalchemy.orm import sessionmaker
from db import engine
from models import *

opened = '''{
    "action": "opened",
    "issue": {
        "html_url": "https://github.com/Mary1509/Practice3/issues/8",
        "id": 947957902,
        "number": 8,
        "state": "open",
        "title": "oop",
        "body": "kkk",
        "user": {
            "login": "Mary1509",
            "html_url": "https://github.com/Mary1509",
            "avatar_url": "https://avatars.githubusercontent.com/u/54399719?v=4"
        },
        "labels": [
            {
                "name": "bug"
            },
            {
                "name": "duplicate"
            },
            {
                "name": "invalid"
            },
            {
                "name": "question"
            }
        ],
        "data": "2021-07-19T19:26:36Z",
        "repository": {
            "name": "Practice3",
            "html_url": "https://github.com/Mary1509/Practice3"
        }
    }
}'''


def parseJson(dataJson):
    return json.loads(dataJson, object_hook=lambda d: SimpleNamespace(**d))

def addDataFromJson(openedJson):

    data = parseJson(openedJson)

    Session = sessionmaker()
    Session.configure(bind=engine)

    issue = Issue(IssueId=data.issue.id,
                  HtmlUrl=data.issue.html_url,
                  Number=data.issue.number,
                  Title=data.issue.title,
                  Body=data.issue.body)

    user = User(UserId=data.issue.user.login,
                HtmlUrl=data.issue.user.html_url,
                AvatarUrl=data.issue.user.avatar_url)

    action = Action(Title=data.action)

    labels = []
    for item in data.issue.labels:
        label = Label(item.name)
        labels.append(label)

    state = State(Title=data.issue.state)

    with Session() as session:
        session.add(issue)
        session.add(user)
        session.add(action)
        session.add_all(labels)
        session.add(state)
        session.flush()

    for item in labels:
        print(item)
    print(issue)
    print(user)
    print(action)
    print(state)

addDataFromJson(opened)