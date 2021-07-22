from flask import Flask
from db import db_url
from querys import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/issues/by-label/<label>", methods=['GET'])
def getIssuesByLabel(label):
    return getIssuesByLabelQuery(label)


@app.route("/issues/", methods=['GET'])
def getIssues():
    return getIssuesQuery()


@app.route("/issues/by-id/<int:id>", methods=['GET'])
def getIssueById(id=None):
    return getIssuesByIdQuery(id)


@app.route("/labels/", methods=['GET'])
def getLabels():
    return getLabelsQuery()


@app.route("/states/", methods=['GET'])
def getStates():
    return getStatesQuery()


@app.route("/actions/", methods=['GET'])
def getActions():
    return getActionsQuery()


@app.route("/users/", methods=['GET'])
def getUsers():
    return getUsersQuery()


if __name__ == '__main__':
    app.run(debug=True)
