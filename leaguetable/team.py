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

    def __repr__(self):
        """
        Provides an interface for python to represent the class.

        """
        return u'{}'.format(
            self.team_name,
        )

    def __dict__(self):
        """
        Returns a dictionary representation of the object

        """
        return {
            u'team_name': self.team_name,
        }

    def __lt__(self, other):
        return self.team_name > other.team_name

    def __eq__(self, other):
        return self.team_name == other.team_name
