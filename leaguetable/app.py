import logging

from leaguetable import match_parser
from leaguetable import league

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger('league.app')


class LeagueApp(object):
    def __init__(self, league_name='Futbol', input_type='file', filename=None):
        self.mp = match_parser.MatchParser()
        self.league = league.League(league_name)

        if input_type == 'raw':
            logger.debug('Raw input chosen')
            self.input = self.input_raw
        elif input_type == 'file':
            if filename:
                logger.debug('File input chosen')
                self.input = self.input_file
                self.filename = filename
            else:
                logger.error('No results file provided')
                raise IOError('No results file provided')

    def run(self):
        self.input()

        table_out = '\nLeague Table:\n\n'
        for row in self.league.get_league_table:
            table_out += '{r[position]}. '.format(r=row)
            table_out += ', '.join([unicode(row[a]) for a in ['team'] + self.league.display_attrs])
            table_out += 'pts\n'

        return table_out

    def input_raw(self):
        match_result = 'start'
        print('Enter match results (leave blank or hit CTRL-D when done)')
        while match_result:
            try:
                match_result = raw_input(': ')
            except EOFError:
                break

            if match_result:
                try:
                    self.league.add_match(self.mp.parse(match_result))
                except (IndexError, ValueError) as e:
                    logger.exception('Could not parse the result: {}'.format(match_result))
                    print('Invalid input, ignored {}'.format(match_result))

    def input_file(self):
        try:
            with open(self.filename) as results:
                for line in results:
                    self.league.add_match(self.mp.parse(line))
        except IOError:
            raise IOError('File {} not found or invalid.'.format(self.filename))
