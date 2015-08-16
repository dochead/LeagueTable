import unittest

from leaguetable import match_parser
from leaguetable.league import League


class TestMatchParser(unittest.TestCase):
    def test_parse(self):
        mp = match_parser.MatchParser()
        l = League('Futbolico')

        l.add_match(mp.parse('Lions 3, Snakes 3'))
        l.add_match(mp.parse('Tarantulas 1, FC Awesome 0'))
        l.add_match(mp.parse('Lions 1, FC Awesome 1'))
        l.add_match(mp.parse('Tarantulas 3, Snakes 1'))
        l.add_match(mp.parse('Lions 4, Grouches 0'))

        self.assertEqual(
            l.get_league_table,
            [
                {u'points': 6, u'position': 1, u'team': 'Tarantulas'},
                {u'points': 5, u'position': 2, u'team': 'Lions'},
                {u'points': 1, u'position': 3, u'team': 'FC Awesome'},
                {u'points': 1, u'position': 3, u'team': 'Snakes'},
                {u'points': 0, u'position': 5, u'team': 'Grouches'}
            ]
        )
