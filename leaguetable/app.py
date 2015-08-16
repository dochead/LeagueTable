import logging

from leaguetable import match_parser
from leaguetable import league
from leaguetable import match

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(u'league.app')


class LeagueApp(object):
    def __init__(self, league_name=u'Futbol', input_type='file', filename=None):
        self.mp = match_parser.MatchParser()
        self.league = league.League(league_name)

        if input_type == u'raw':
            logger.debug('Raw input chosen')
            self.input = self.input_raw
        elif input_type == u'file':
            if filename:
                logger.debug(u'File input chosen')
                self.input = self.input_file
                self.filename = filename
            else:
                logger.error(u'No results file provided')
                raise IOError(u'No results file provided')

    def run(self):
        self.input()

        table_out = u'\nLeague Table:\n\n'
        for row in self.league.get_league_table:
            table_out += u'{r[position]}. '.format(r=row)
            table_out += u', '.join([unicode(row[a]) for a in [u'team'] + self.league.display_attrs])
            table_out += u'pts\n'

        return table_out

    def input_raw(self):
        match_result = u'start'
        print(u'Enter match results (leave blank or hit CTRL-D when done)')
        while match_result:
            try:
                match_result = raw_input(u': ').decode('utf-8')
            except EOFError:
                break

            if match_result:
                # noinspection PyUnusedLocal
                try:
                    self.league.add_match(self.mp.parse(match_result))
                except (IndexError, ValueError, match.MatchTeamException, match.MatchScoreException) as e:
                    logger.exception(u'Could not parse the result: {}'.format(match_result))
                    print(u'Invalid input, ignored {}'.format(match_result))

    def input_file(self):
        try:
            with open(self.filename) as results:
                for line in results:
                    self.league.add_match(self.mp.parse(line))
        except IOError:
            raise IOError(u'File {} not found or invalid.'.format(self.filename))
