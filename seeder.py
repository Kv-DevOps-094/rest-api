from models import *


class DatabaseSeeder:
    def __init__(self):
        self.users = [
            User(UserId='Mary1509',
                 HtmlUrl='https://github.com/Mary1509',
                 AvatarUrl='https://avatars.githubusercontent.com/u/54399719?v=4')
        ]

        self.actions = [
            Action(ActionId=1, Title='opened'),
            Action(ActionId=2, Title='assigned'),
            Action(ActionId=3, Title='closed'),
        ]

        self.issues = [

            Issue(IssueId=944298295, HtmlUrl='https://github.com/Mary1509/Practice3/issues/3', Number=3,
                  Title='Third issue title', Body='Comment here'),
            Issue(IssueId=944298296, HtmlUrl='https://github.com/Mary1509/Practice3/issues/4', Number=4,
                  Title='Fourth issue title', Body='Comment here'),
            Issue(IssueId=944298297, HtmlUrl='https://github.com/Mary1509/Practice3/issues/5', Number=5,
                  Title='Fifth issue title', Body='Comment here')
        ]

        self.states = [
            State(StateId=1, Title="open"),
            State(StateId=2, Title="closed")
        ]

        self.labels = [
            Label(LabelId=1, Title="User story"),
            Label(LabelId=2, Title="Test case"),
            Label(LabelId=3, Title="Bug report"),
        ]

        self.issueActions = [
            IssueAction(IssueId=944298295, ActionId=1, UserId='Mary1509', ModifiedDate='2021-07-14 09:03:03'),
            IssueAction(IssueId=944298296, ActionId=1, UserId='Mary1509', ModifiedDate='2021-07-14 09:13:03'),
            IssueAction(IssueId=944298297, ActionId=1, UserId='Mary1509', ModifiedDate='2021-07-14 09:23:03'),
            IssueAction(IssueId=944298295, ActionId=2, UserId='Mary1509', ModifiedDate='2021-07-14 10:13:03'),
            IssueAction(IssueId=944298296, ActionId=2, UserId='Mary1509', ModifiedDate='2021-07-14 09:23:03'),
            IssueAction(IssueId=944298297, ActionId=2, UserId='Mary1509', ModifiedDate='2021-07-14 09:33:03'),
            IssueAction(IssueId=944298295, ActionId=3, UserId='Mary1509', ModifiedDate='2021-07-14 11:03:03'),
            IssueAction(IssueId=944298296, ActionId=3, UserId='Mary1509', ModifiedDate='2021-07-14 09:13:03'),
            IssueAction(IssueId=944298297, ActionId=3, UserId='Mary1509', ModifiedDate='2021-07-14 09:23:03')
        ]

        self.issueLabels = [
            IssueLabel(IssueId=944298295, LabelId=1),
            IssueLabel(IssueId=944298295, LabelId=2),
            IssueLabel(IssueId=944298295, LabelId=3),
            IssueLabel(IssueId=944298296, LabelId=1),
            IssueLabel(IssueId=944298296, LabelId=2),
            IssueLabel(IssueId=944298296, LabelId=3),
            IssueLabel(IssueId=944298297, LabelId=1),
            IssueLabel(IssueId=944298297, LabelId=2),
            IssueLabel(IssueId=944298297, LabelId=3)
        ]

        self.issueStates = [
            IssueState(IssueId=944298295, StateId=1, ModifiedDate="2021-07-14 09:03:03"),
            IssueState(IssueId=944298295, StateId=2, ModifiedDate="2021-07-14 11:03:03"),
            IssueState(IssueId=944298296, StateId=1, ModifiedDate="2021-08-14 11:03:03"),
            IssueState(IssueId=944298296, StateId=2, ModifiedDate="2021-08-14 12:03:03"),
            IssueState(IssueId=944298297, StateId=1, ModifiedDate="2021-08-14 12:03:03"),
            IssueState(IssueId=944298297, StateId=2, ModifiedDate="2021-08-14 13:03:03")
        ]

