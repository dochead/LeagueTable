class MatchScoreException(Exception):
    pass


class MatchTeamException(Exception):
    pass


class Match(object):
    def __init__(self, home_team, home_score, away_team, away_score):

        self.home_team = home_team
        self.home_score = home_score
        self.away_team = away_team
        self.away_score = away_score
        self.__validate_scores__(home_score=home_score, away_score=away_score)
        self.__validate_teams__(home_team, away_team)



    @property
    def winner(self):
        if self.home_score > self.away_score:
            return self.home_team
        elif self.home_score < self.away_score:
            return self.away_team
        else:
            return None

    def __validate_scores__(self, **kwargs):
        negs = filter(lambda s: s[1] < 0, kwargs.items())
        if len(negs):
            raise MatchScoreException(u'Score cannot be negative in {} vs. {}: ({})'.format(
                self.home_team.team_name,
                self.away_team.team_name,
                ', '.join(['{}: {}'.format(i[0], i[1]) for i in negs]))
            )

    def __validate_teams__(self, home_team, away_team):
        dupes = True if home_team == away_team else False
        if dupes:
            raise MatchTeamException(u'A team cannot play itself: {} vs. {}'.format(
                self.home_team.team_name,
                self.away_team.team_name)
            )
