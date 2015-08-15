# -*- coding: utf-8 -*-.

import unittest

from leaguetable.team import Team
from leaguetable.match import Match, MatchTeamException, MatchScoreException


class TestMatch(unittest.TestCase):
    def test_team_home_win(self):
        home = Team(u'Liddlypool')
        away = Team(u'Chelski')
        match = Match(home, 1, away, 0)
        self.assertEqual(match.winner, home)

    def test_match_away_win(self):
        home = Team(u'Man Citeh')
        away = Team(u'Gleeds')
        match = Match(home, 1, away, 3)
        self.assertEqual(match.winner, away)

    def test_match_draw(self):
        home = Team(u'East Crom Ganglion')
        away = Team(u'Wensleydale')
        match = Match(home, 0, away, 0)
        self.assertEqual(match.winner, None)

    def test_match_negative(self):
        home = Team(u'Supa Strikers')
        away = Team(u'FC Aqua')
        with self.assertRaises(MatchScoreException):
            Match(home, 0, away, -1)

    def test_match_dupes(self):
        home = Team(u'BK Häcken')
        with self.assertRaises(MatchTeamException):
            Match(home, 0, home, 0)

if __name__ == '__main__':
    unittest.main()
