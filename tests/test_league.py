# -*- coding: utf-8 -*-.

import unittest

from leaguetable.league import League
from leaguetable.match import Match
from leaguetable.team import Team


class TestLeague(unittest.TestCase):
    @staticmethod
    def __gen_matches__():
        teams = [
            Team(u'Gençlerbirliği'),
            Team(u'Feriköy'),
            Team(u'Ankaragücü'),
            Team(u'Kasımpaşa'),
        ]

        matches = [
            Match(teams[0], 1, teams[1], 0),
            Match(teams[0], 2, teams[2], 3),
            Match(teams[0], 3, teams[3], 3),
            Match(teams[1], 1, teams[0], 2),
            Match(teams[1], 0, teams[2], 5),
            Match(teams[1], 1, teams[3], 3),
            Match(teams[2], 1, teams[0], 0),
            Match(teams[2], 1, teams[1], 1),
            Match(teams[2], 3, teams[3], 1),
            Match(teams[3], 6, teams[0], 0),
            Match(teams[3], 2, teams[1], 2),
            Match(teams[3], 4, teams[2], 5),
        ]

        return teams, matches

    def test_create_league(self):
        l = League(u'Süper Lig')
        self.assertEqual(l.league_name, u'Süper Lig')

    def test_add_match(self):
        teams, matches = self.__gen_matches__()
        league = League(u'Süper Lig')

        for m in matches:
            league.add_match(m)

        self.assertEqual(len(league.matches), 12)
        self.assertEqual(len(league.teams), 4)

    def test_get_league(self):
        teams, matches = self.__gen_matches__()
        league = League(u'Süper Lig')

        for m in matches:
            league.add_match(m)

        standings = league.get_league_table()
        self.assertEqual(standings, None)


    if __name__ == '__main__':
        unittest.main()
