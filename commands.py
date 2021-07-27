import json
from types import SimpleNamespace

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from db import engine
from models import *

opened = '''{
    "action": "opened1",
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

other = '''{
    "action": "labeled",
    "issue": {
        "id": 947957902,
        "state": "closed",
        "user": {
            "login": "Mary1509",
            "html_url": "https://github.com/Mary1509",
            "avatar_url": "https://avatars.githubusercontent.com/u/54399719?v=4"
        },
        "data": "2021-07-19T19:26:36Z"
    }
}'''


def parseJson(dataJson):
    return json.loads(dataJson, object_hook=lambda d: SimpleNamespace(**d))


def addUser(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)
    user = User(UserId=data.issue.user.login,
                HtmlUrl=data.issue.user.html_url,
                AvatarUrl=data.issue.user.avatar_url)
    query = session.query(User).filter(User.UserId == user.UserId)
    try:
        user = query.one()
    except NoResultFound:
        session.add(user)
    finally:
        session.commit()
        return user


def addAction(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)
    action = Action(Title=data.action)
    query = session.query(Action).filter(Action.Title == action.Title)
    try:
        action = query.one()
        print(f"{action} exists")
    except NoResultFound:
        session.add(action)
        print(f"{action} added")
    finally:
        session.commit()
        return action


def addState(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)
    state = State(Title=data.issue.state)

    query = session.query(State).filter(State.Title == state.Title)
    try:
        state = query.one()
    except NoResultFound:
        session.add(state)
    finally:
        session.commit()
        return state


def addLabel(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)
    labels = []
    for item in data.issue.labels:
        label = Label(item.name)
        labels.append(label)
    ls = []
    for label in labels:
        query = session.query(Label).filter(Label.Title == label.Title)
        try:
            label = query.one()
            ls.append(label)
        except NoResultFound:
            session.add(label)
            session.commit()
            ls.append(label)
    return ls


def addIssue(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)
    issue = Issue(IssueId=data.issue.id,
                  HtmlUrl=data.issue.html_url,
                  Number=data.issue.number,
                  Title=data.issue.title,
                  Body=data.issue.body)

    query = session.query(Issue).filter(Issue.IssueId == issue.IssueId)
    try:
        issue = query.one()
    except NoResultFound:
        session.add(issue)
    finally:
        session.commit()
        return issue


def addIssueActionLabelState(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)

    issue = Issue(IssueId=data.issue.id,
                  HtmlUrl=data.issue.html_url,
                  Number=data.issue.number,
                  Title=data.issue.title,
                  Body=data.issue.body)

    query = session.query(Issue).filter(Issue.IssueId == issue.IssueId)
    try:
        issue = query.one()
    except NoResultFound:
        issueAction = IssueAction(UserId=data.issue.user.login,
                                  ModifiedDate=data.issue.data)
        issueAction.Action = addAction(dataJson)
        issue.Actions.append(issueAction)

        issueState = IssueState(ModifiedDate=data.issue.data)
        issueState.State = addState(dataJson)
        issue.States.append(issueState)

        issueLabel = IssueLabel()
        labels = addLabel(dataJson)
        for label in labels:
            issueLabel.Label = label
            issue.Labels.append(issueLabel)
            session.add(issue)
        session.add(issue)
    finally:
        session.commit()

    return issue


def addIssueActionState(dataJson):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    data = parseJson(dataJson)

    query = session.query(Issue).filter(Issue.IssueId == data.issue.id)
    try:
        issue = query.one()

        issueAction = IssueAction(UserId=data.issue.user.login,
                                  ModifiedDate=data.issue.data)
        issueAction.Action = addAction(dataJson)
        issue.Actions.append(issueAction)

        issueState = IssueState(ModifiedDate=data.issue.data)
        issueState.State = addState(dataJson)
        issue.States.append(issueState)
        session.add(issue)
    except NoResultFound as ex:
        print(ex)
    finally:
        session.commit()
    return issue


# addUser(opened)
# addIssueActionLabelState(opened)
addIssueActionState(other)
