from flask import jsonify
from sqlalchemy.orm import sessionmaker

from db import engine
from models import *


def getIssuesByLabelQuery(filters: str):
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()

    query = session.query(
        Issue.IssueId.label("IssueId"),
        State.Title.label("State"),
        Issue.Title.label("Issue"),
        Issue.HtmlUrl.label("IssueHtmlUrl"),
        User.UserId.label("UserId"),
        User.HtmlUrl.label("UserHtmlUrl"),
        User.AvatarUrl.label("UserAvatarUrl"),
        IssueAction.ModifiedDate.label("ModifiedDate"),
        Action.Title.label("Action")
    ). \
        join(IssueLabel). \
        join(Label). \
        join(IssueAction). \
        join(Action). \
        join(User). \
        join(IssueState). \
        join(State). \
        filter(Label.Title.contains(filters)). \
        order_by(Issue.IssueId, IssueAction.ModifiedDate). \
        all()

    return jsonify([
        {
            'IssueId': item.IssueId,
            'State': item.State,
            'Issue': item.Issue,
            'IssueHtmlUrl': item.IssueHtmlUrl,
            'UserId': item.UserId,
            'UserHtmlUrl': item.UserHtmlUrl,
            'UserAvatarUrl': item.UserAvatarUrl,
            'ModifiedDate': item.ModifiedDate,
            'Action': item.Action,
        } for item in query])


def getLabelsQuery():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    query = session.query(Label).all()
    return jsonify([
        {
            'LabelId': item.LabelId,
            'Title': item.Title,
        } for item in query])


def getStatesQuery():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    query = session.query(State).all()
    return jsonify([
        {
            'StateId': item.StateId,
            'Title': item.Title,
        } for item in query])


def getActionsQuery():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    query = session.query(Action).all()
    return jsonify([
        {
            'ActionId': item.ActionId,
            'Title': item.Title,
        } for item in query])


def getUsersQuery():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    query = session.query(User).all()
    return jsonify([
        {
            'UserId': item.UserId,
            'HtmlUrl': item.HtmlUrl,
            'AvatarUrl': item.AvatarUrl,
        } for item in query])


def getIssuesQuery():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    query = session.query(Issue).all()
    return jsonify([
        {
            'IssueId': item.IssueId,
            'HtmlUrl': item.HtmlUrl,
            'Number': item.Number,
            'Title': item.Title,
            'Body': item.Body,
        } for item in query])
