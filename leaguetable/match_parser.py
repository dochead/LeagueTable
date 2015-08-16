import logging

from leaguetable.team import Team
from leaguetable.match import Match

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger('league.parser')


class MatchParser(object):
    def parse(self, match_result):
        """
        Takes a match and parses it into objects, then adds the match to the league. It splits the line
        across the comma for each team and then further along the last space to seperate team and score,
        it *could* potentially use a regex such as (.*) ([0-9]+) ?, ?(.*) ?([0-9]+)

        :param match_result:
        """

        teams = match_result.split(',')
        team_types = ['home', 'away']
        match_data = {}
        try:
            for i, result in enumerate(teams):
                score_list = result.strip().rsplit(' ', 1)
                match_data.update({
                    u'{}_team'.format(team_types[i]): Team(score_list[0]),
                    u'{}_score'.format(team_types[i]): int(score_list[1]),
                })
            match = Match(**match_data)
        except (IndexError, ValueError) as e:
            logger.exception('Error in parsing: {}'.format(match_result))
            raise e

        return match

