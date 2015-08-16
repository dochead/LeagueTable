class MatchScoreException(Exception):
    pass


class MatchTeamException(Exception):
    pass


class Match(object):
    def __init__(self, home_team, home_score, away_team, away_score):

        """
        Represents a match between 2 teams and the final score of the game, designated home and
        away. Also provides methods to determine the winner and validate the input provided
        when initialising the class.

        :param home_team:
        :param home_score:
        :param away_team:
        :param away_score:
        """
        self.home_team = home_team
        self.home_score = home_score
        self.away_team = away_team
        self.away_score = away_score
        self.__validate_scores__(home_score=home_score, away_score=away_score)
        self.__validate_teams__(home_team, away_team)

    @property
    def result(self):
        if self.home_score > self.away_score:
            return {
                u'home': u'won',
                u'away': u'lost'
            }
        elif self.home_score < self.away_score:
            return {
                u'home': u'lost',
                u'away': u'won'
            }
        else:
            return {
                u'home': u'drew',
                u'away': u'drew'
            }

    def __validate_scores__(self, **kwargs):
        negs = filter(lambda s: s[1] < 0, kwargs.items())
        if len(negs):
            raise MatchScoreException(u'Score cannot be negative in {} vs. {}: ({})'.format(
                self.home_team.team_name,
                self.away_team.team_name,
                u', '.join([u'{}: {}'.format(i[0], i[1]) for i in negs]))
            )

    def __validate_teams__(self, home_team, away_team):
        dupes = True if home_team == away_team else False
        if dupes:
            raise MatchTeamException(u'A team cannot play itself: {} vs. {}'.format(
                self.home_team.team_name,
                self.away_team.team_name)
            )
