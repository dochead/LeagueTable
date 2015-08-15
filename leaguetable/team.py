class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name

        self.matches = []

        self.won = 0
        self.drew = 0
        self.lost = 0
        self.goals_for = 0
        self.goals_against = 0

    def __repr__(self):
        return '{} - Pl: {}, W: {}, L: {}, D:{}, GF: {}, GA: {}, GD: {}'.format(
            self.team_name,
            len(self.matches),
            self.played,
            self.won,
            self.drew,
            self.lost,
            self.goals_for,
            self.goals_against,
            self.goal_difference
        )

    @property
    def played(self):
        return self.won + self.drew + self.lost

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against
