from leaguetable import match_parser
from leaguetable import league


class LeagueApp(object):
    def __init__(self, league_name='Futbol', input_type='file', filename=None):
        self.mp = match_parser.MatchParser()
        self.league = league.League(league_name)

        if input_type == 'raw':
            self.input = self.input_raw
        elif input_type == 'file':
            if filename:
                self.input = self.input_file
                self.filename = filename
            else:
                raise IOError('No results file provided')

    def run(self):
        self.input()

        table_out = '\nLeague Table:'
        for row in self.league.get_league_table():
            table_out += '{r[position]}. {r[team]}, {r[points]}pts\n'.format(r=row)

        return table_out

    def input_raw(self):
        match_result = 'start'
        print('Enter match results (leave blank when done)')
        while match_result:
            match_result = raw_input(': ')
            if match_result:
                self.league.add_match(self.mp.parse(match_result))

    def input_file(self):
        try:
            with open(self.filename) as results:
                for line in results:
                    self.league.add_match(self.mp.parse(line))
        except IOError, e:
            raise IOError('File {} not found or invalid.'.format(self.filename))
