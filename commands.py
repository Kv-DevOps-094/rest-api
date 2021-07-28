import json
from types import SimpleNamespace
from sqlalchemy.exc import NoResultFound
from db import db_session
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
    data = parseJson(dataJson)
    user = User(UserId=data.issue.user.login,
                HtmlUrl=data.issue.user.html_url,
                AvatarUrl=data.issue.user.avatar_url)
    session = db_session()
    query = session.query(User).filter(User.UserId == user.UserId)
    try:
        user = query.one()
        print(f"Function addUser() - user exists")
    except NoResultFound:
        session.add(user)
        print(f"Function addUser() - user added")
    finally:
        session.commit()
        print(f"{user}")
        return user


def addAction(dataJson):
    data = parseJson(dataJson)
    action = Action(Title=data.action)
    session = db_session()
    session.expire_on_commit = False
    query = session.query(Action).filter(Action.Title == action.Title)
    try:
        action = query.one()
        print(f"Function addAction() - action exist")
    except NoResultFound:
        session.add(action)
        print(f"Function addAction() - action added")
    finally:
        session.commit()
        session.close()
        print(f"{action}")
        return action


def addState(dataJson):
    data = parseJson(dataJson)

    state = State(Title=data.issue.state)

    session = db_session()
    session.expire_on_commit = False
    query = session.query(State).filter(State.Title == state.Title)

    try:
        state = query.one()
        print(f"Function addState() - state exist")
    except NoResultFound:
        session.add(state)
        print(f"Function addState() - state added")
    finally:
        session.commit()
        session.close()
        print(f"{state}")
        return state


def addLabel(dataJson):
    session = db_session()
    session.expire_on_commit = False

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
            print(f"Function addLabel() - label exist")
        except NoResultFound:
            session.add(label)
            session.commit()
            ls.append(label)
            print(f"{label}")
    session.commit()
    session.close()
    return ls


def addIssue(dataJson):
    data = parseJson(dataJson)
    issue = Issue(IssueId=data.issue.id,
                  HtmlUrl=data.issue.html_url,
                  Number=data.issue.number,
                  Title=data.issue.title,
                  Body=data.issue.body)

    session = db_session()
    query = session.query(Issue).filter(Issue.IssueId == issue.IssueId)
    try:
        issue = query.one()
        print(f"Function addIssue() - issue exist")
    except NoResultFound:
        session.add(issue)
        print(f"Function addIssue() - issue added")
    finally:
        session.commit()
        print(f"{issue}")
    return issue


def addIssueActionLabelState(dataJson):
    data = parseJson(dataJson)
    issue = Issue(IssueId=data.issue.id,
                  HtmlUrl=data.issue.html_url,
                  Number=data.issue.number,
                  Title=data.issue.title,
                  Body=data.issue.body)

    session = db_session()
    query = session.query(Issue).filter(Issue.IssueId == issue.IssueId)

    try:
        issue = query.one()
        print(f"Function addIssueActionLabelState() - issue exist")
    except NoResultFound:
        issueAction = IssueAction(UserId=data.issue.user.login,
                                  ModifiedDate=data.issue.data)
        issueAction.Action = addAction(dataJson)
        issue.Actions.append(issueAction)

        issueState = IssueState(ModifiedDate=data.issue.data)
        issueState.State = addState(dataJson)
        issue.States.append(issueState)
        labels = []
        for label in addLabel(dataJson):
            labels.append(label)

        for label in labels:
            issueLabel = IssueLabel()
            issueLabel.IssueId = issue.IssueId
            issueLabel.LabelId = label.LabelId
            session.add(issueLabel)
        session.add(issue)
        print(f"Function addIssueActionLabelState() - issue added")
    finally:
        session.commit()
        print(f"{issue}")
    return issue


def addIssueActionState(dataJson):
    data = parseJson(dataJson)
    session = db_session()
    query = session.query(Issue).filter(Issue.IssueId == data.issue.id)
    issue = None
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


# addLabel(opened)
addUser(opened)
# Add data from new issue
addIssueActionLabelState(opened)

addUser(other)
# Add changed status for issue
addIssueActionState(other)
