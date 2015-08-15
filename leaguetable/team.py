class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name

    def __repr__(self):
        return u'{}'.format(
            self.team_name,
        )
