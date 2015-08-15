class League(object):
    def __init__(self, league_name, win_points=3, draw_points=1, lose_points=0, tiebreak=None):
        self.league_name = league_name
        self._teams = set()
        self.matches = []
        self.win_points = win_points
        self.draw_points = draw_points
        self.lose_points = lose_points
        self.tiebreak = tiebreak if tiebreak else self.__tiebreak_method__

    def __tiebreak_method__(self, *args):
        pass

    def add_match(self, match):
        self._teams.add(match.home_team)
        self._teams.add(match.away_team)
        self.__calc_league_stats__(match)
        self.matches.append(match)

    def __calc_league_stats__(self, match):
        pass

    def get_league_table(self):
        return self.tiebreak(self.teams)

    @property
    def teams(self):
        return self._teams
