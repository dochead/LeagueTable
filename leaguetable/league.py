class League(object):
    def __init__(self, league_name):
        self.league_name = league_name
        self._teams = set()
        self.matches = []

    def add_match(self, match):
        self._teams.add(match.home_team)
        self._teams.add(match.away_team)
        self.matches.append(match)

    @property
    def teams(self):
        return self._teams
