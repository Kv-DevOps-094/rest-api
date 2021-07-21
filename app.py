from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker

from db import db_url, engine
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/", methods=['GET'])
def data():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()

    query = session.query(Issue.IssueId, State.Title, Issue.Title, Issue.HtmlUrl, User.UserId, User.HtmlUrl,
                          User.AvatarUrl, IssueAction.ModifiedDate, Action.Title). \
        join(IssueLabel). \
        join(Label). \
        join(IssueAction). \
        join(Action). \
        join(User). \
        join(IssueState). \
        join(State).all()

    return jsonify([
        {
            'IssueId': item.IssueId,
            'StateTitle': item.Title,
            'IssueTitle': [],
            'IssueHtmlUrl': [],
            'UserId': item.UserId,
            'UserHtmlUrl': item.HtmlUrl,
            'UserAvatarUrl': item.AvatarUrl,
            'IssueActionModifiedDate': item.ModifiedDate,
            'ActionTitle': [],
        } for item in query
    ])


if __name__ == '__main__':
    app.run(debug=True)
