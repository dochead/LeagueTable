class Team(object):
    def __init__(self, team_name):
        """
        The Team object contains relevant attributes & methods representing a football team. This
        could include their name, nickname, players, location, etc. Methods that could be added
        include match listings, pulling goal difference stats, etc. It does not contain a list of
        matches or any leagues that the may be in at the moment in an attempt to avoid circular
        references.

        :param team_name:
        """
        self.team_name = team_name
        self.won = 0
        self.drew = 0
        self.lost = 0
        self.goals_for = 0
        self.goals_against = 0

    def __repr__(self):
        """
        Provides an interface for python to represent the class.

        """
        return '{} - Pl: {}, W: {}, L: {}, D:{}, GF: {}, GA: {}, GD: {}'.format(
            self.team_name,
            self.played,
            self.won,
            self.drew,
            self.lost,
            self.goals_for,
            self.goals_against,
            self.goal_difference
        )

    def __dict__(self):
        """
        Returns a dictionary representation of the object

        """
        return {
            'team_name': self.team_name,
        }

    @property
    def played(self):
        return self.won + self.drew + self.lost


    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against
