from dataclasses import dataclass

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'
    UserId = Column(String, primary_key=True)
    HtmlUrl = Column(String, unique=True)
    AvatarUrl = Column(String, unique=True)
    IssueActions = relationship("IssueAction")

    def __init__(self, UserId, HtmlUrl, AvatarUrl):
        self.UserId = UserId
        self.HtmlUrl = HtmlUrl
        self.AvatarUrl = AvatarUrl

    def __repr__(self):
        return f"UserId: {self.UserId}, HtmlUrl: {self.HtmlUrl}, AvatarUrl: {self.AvatarUrl}"


class IssueAction(Base):
    __tablename__ = 'IssueActions'
    IssueId = Column(ForeignKey('Issues.IssueId'), primary_key=True)
    ActionId = Column(ForeignKey('Actions.ActionId'), primary_key=True)
    UserId = Column(String, ForeignKey('Users.UserId'))
    ModifiedDate = Column(DateTime)
    # Users = relationship('User', backref='issueActions')
    Action = relationship("Action")
    # Action = relationship("Action", back_populates="Issues")
    # Issue = relationship("Issue", back_populates="Actions")

    def __repr__(self):
        return f"IssueId: {self.IssueId}, ActionId: {self.ActionId}, UserId: {self.UserId}, ModifiedDate: {self.ModifiedDate}"


class Issue(Base):
    __tablename__ = 'Issues'
    IssueId = Column(Integer, primary_key=True)
    HtmlUrl = Column(String)
    Number = Column(Integer)
    Title = Column(String)
    Body = Column(String)
    Actions = relationship("IssueAction")
    States = relationship("IssueState")
    Labels = relationship("IssueLabel")

    # Actions = relationship("IssueAction", back_populates="Issue")
    # States = relationship("IssueState", back_populates="Issue")
    # Labels = relationship("IssueLabel", back_populates="Issue")

    # def __init__(self, IssueId, HtmlUrl, Number, Title, Body):
    #     self.IssueId = IssueId
    #     self.HtmlUrl = HtmlUrl
    #     self.Number = Number
    #     self.Title = Title
    #     self.Body = Body

    def __repr__(self):
        return f"IssueId: {self.IssueId}, HtmlUrl: {self.HtmlUrl}, Number: {self.Number}, Title: {self.Title}, Body: {self.Body}"


class Action(Base):
    __tablename__ = 'Actions'
    ActionId = Column(Integer, primary_key=True)
    Title = Column(String, unique=True)
    # Issues = relationship("IssueAction", back_populates="Action")

    def __init__(self, Title):
        # self.ActionId = ActionId
        self.Title = Title

    def __repr__(self):
        return f"ActionId: {self.ActionId}, Title: {self.Title}"


class Label(Base):
    __tablename__ = 'Labels'
    LabelId = Column(Integer, primary_key=True)
    Title = Column(String, unique=True)
    # Issues = relationship("IssueLabel", back_populates="Label")

    def __init__(self, Title):
        # self.LabelId = LabelId
        self.Title = Title

    def __repr__(self):
        return f"LabelId: {self.LabelId}, Title: {self.Title}"


class State(Base):
    __tablename__ = 'States'
    StateId = Column(Integer, primary_key=True)
    Title = Column(String, unique=True)
    # Issues = relationship("IssueState", back_populates="State")

    def __init__(self, Title):
        # self.StateId = StateId
        self.Title = Title

    def __repr__(self):
        return f"StateId: {self.StateId}, Title: {self.Title}"


class IssueLabel(Base):
    __tablename__ = 'IssueLabels'
    IssueId = Column(ForeignKey('Issues.IssueId'), primary_key=True)
    LabelId = Column(ForeignKey('Labels.LabelId'), primary_key=True)
    Label = relationship("Label")
    # Label = relationship("Label", back_populates="Issues")
    # Issue = relationship("Issue", back_populates="Labels")

    def __repr__(self):
        return f"IssueId: {self.IssueId}, LabelId: {self.LabelId}"


class IssueState(Base):
    __tablename__ = 'IssueStates'
    IssueId = Column(ForeignKey('Issues.IssueId'), primary_key=True)
    StateId = Column(ForeignKey('States.StateId'), primary_key=True)
    ModifiedDate = Column(DateTime)
    State = relationship("State")
    #
    # State = relationship("State", back_populates="Issues")
    # Issue = relationship("Issue", back_populates="States")

    def __repr__(self):
        return f"IssueId: {self.IssueId}, StateId: {self.StateId}, ModifiedDate: {self.ModifiedDate}"
