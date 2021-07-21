from dataclasses import dataclass

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


@dataclass
class User(Base):
    __tablename__ = 'Users'
    UserId = Column(String, primary_key=True)
    HtmlUrl = Column(String, unique=True)
    AvatarUrl = Column(String, unique=True)

    # def __repr__(self):
    #     return f"UserId: {self.UserId}, HtmlUrl: {self.HtmlUrl}, AvatarUrl: {self.AvatarUrl}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@dataclass
class Issue(Base):
    __tablename__ = 'Issues'
    IssueId = Column(Integer, primary_key=True)
    HtmlUrl = Column(String)
    Number = Column(Integer)
    Title = Column(String)
    Body = Column(String)

    # def __repr__(self):
    #     return f"IssueId: {self.IssueId}, HtmlUrl: {self.HtmlUrl}, Number: {self.Number}, Title: {self.Title}, Body: {self.Body}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict



@dataclass
class Action(Base):
    __tablename__ = 'Actions'
    ActionId = Column(Integer, primary_key=True)
    Title = Column(String, unique=True)

    # def __repr__(self):
    #     return f"ActionId: {self.ActionId}, Title: {self.Title}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@dataclass
class Label(Base):
    __tablename__ = 'Labels'
    LabelId = Column(Integer, primary_key=True)
    Title = Column(String, unique=True)

    # def __repr__(self):
    #     return f"LabelId: {self.LabelId}, Title: {self.Title}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@dataclass
class State(Base):
    __tablename__ = 'States'
    StateId = Column(Integer, primary_key=True)
    Title = Column(String, unique=True)

    # def __repr__(self):
    #     return f"StateId: {self.StateId}, Title: {self.Title}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@dataclass
class IssueAction(Base):
    __tablename__ = 'IssueActions'
    IssueId = Column(Integer, ForeignKey('Issues.IssueId'), primary_key=True)
    ActionId = Column(Integer, ForeignKey('Actions.ActionId'), primary_key=True)
    UserId = Column(String, ForeignKey('Users.UserId'))
    ModifiedDate = Column(DateTime)
    Users = relationship('User', backref='issueActions')
    Issues = relationship(Issue, backref=backref("IssueActions"))
    Actions = relationship(Action, backref=backref("IssueActions"))

    # def __repr__(self):
    #     return f"IssueId: {self.IssueId}, ActionId: {self.ActionId}, UserId: {self.UserId}, ModifiedDate: {self.ModifiedDate}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@dataclass
class IssueLabel(Base):
    __tablename__ = 'IssueLabels'
    IssueId = Column(Integer, ForeignKey('Issues.IssueId'), primary_key=True)
    LabelId = Column(Integer, ForeignKey('Labels.LabelId'), primary_key=True)
    Issues = relationship(Issue, backref=backref("IssueLabels"))
    Labels = relationship(Label, backref=backref("IssueLabels"))

    # def __repr__(self):
    #     return f"IssueId: {self.IssueId}, LabelId: {self.LabelId}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@dataclass
class IssueState(Base):
    __tablename__ = 'IssueStates'
    IssueId = Column(Integer, ForeignKey('Issues.IssueId'), primary_key=True)
    StateId = Column(Integer, ForeignKey('States.StateId'), primary_key=True)
    ModifiedDate = Column(DateTime)
    Issues = relationship(Issue, backref=backref("IssueStates"))
    States = relationship(State, backref=backref("IssueStates"))

    # def __repr__(self):
    #     return f"IssueId: {self.IssueId}, StateId: {self.StateId}, ModifiedDate: {self.ModifiedDate}"
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
