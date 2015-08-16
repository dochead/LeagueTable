import unittest

from leaguetable import match_parser
from leaguetable.league import League


class TestMatchParser(unittest.TestCase):
    def test_parse(self):
        mp = match_parser.MatchParser()
        l = League('Futbolico')

        l.add_match(mp.parse(u'Lions 3, Snakes 3'))
        l.add_match(mp.parse(u'Tarantulas 1, FC Awesome 0'))
        l.add_match(mp.parse(u'Lions 1, FC Awesome 1'))
        l.add_match(mp.parse(u'Tarantulas 3, Snakes 1'))
        l.add_match(mp.parse(u'Lions 4, Grouches 0'))

        self.assertEqual(
            l.get_league_table,
            [
                {u'points': 6, u'position': 1, u'team': u'Tarantulas'},
                {u'points': 5, u'position': 2, u'team': u'Lions'},
                {u'points': 1, u'position': 3, u'team': u'FC Awesome'},
                {u'points': 1, u'position': 3, u'team': u'Snakes'},
                {u'points': 0, u'position': 5, u'team': u'Grouches'}
            ]
        )

    def test_parse_nonsense(self):
        mp = match_parser.MatchParser()
        l = League(u'Futbolico')

        with self.assertRaises(ValueError):
            l.add_match(mp.parse(u'No football for you!'))


if __name__ == u'__main__':
    unittest.main()
