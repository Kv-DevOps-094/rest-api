from flask import jsonify
from sqlalchemy import func, select
from db import dbSession
from models import *


def getIssuesByLabelQuery(label: str):
    """
    :param label: for filtering issues
    :return: list of issues from db
    """
    label = str.lower(label)
    print(label)
    session = dbSession()

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
        filter(func.lower(Label.Title).contains(label)). \
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


def getIssuesByIdQuery(issueId):
    """
    :param issueId: for filtering issues
    :return: list of issues from db
    """
    session = dbSession()

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
        filter(Issue.IssueId == issueId). \
        order_by(IssueAction.ModifiedDate). \
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
    """
    :return: list of labels from db
    """
    session = dbSession()
    query = session.query(Label).all()
    return jsonify([
        {
            'LabelId': item.LabelId,
            'Title': item.Title,
        } for item in query])


def getStatesQuery():
    """
    :return: list of states from db
    """
    session = dbSession()
    query = session.query(State).all()
    return jsonify([
        {
            'StateId': item.StateId,
            'Title': item.Title,
        } for item in query])


def getActionsQuery():
    """
    :return: list of actions from db
    """
    session = dbSession()
    query = session.query(Action).all()
    return jsonify([
        {
            'ActionId': item.ActionId,
            'Title': item.Title,
        } for item in query])


def getUsersQuery():
    session = dbSession()
    query = session.query(User).all()
    return jsonify([
        {
            'UserId': item.UserId,
            'HtmlUrl': item.HtmlUrl,
            'AvatarUrl': item.AvatarUrl,
        } for item in query])


def getIssuesQuery():
    """
    :return: list of issues from db
    """
    session = dbSession()
    query = session.query(Issue).all()
    return jsonify([
        {
            'IssueId': item.IssueId,
            'HtmlUrl': item.HtmlUrl,
            'Number': item.Number,
            'Title': item.Title,
            'Body': item.Body,
        } for item in query])