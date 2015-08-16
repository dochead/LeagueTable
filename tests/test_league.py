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
            Match(teams[0], 6, teams[2], 6),
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

    def test_calc_standings(self):
        home = Team(u'TOP Oss')
        away = Team(u'Go Ahead Eagles')
        m = Match(home, 0, away, 3)
        l = League(u'Eerste Divisie')

        match_outcome = l.__calc_league_stats__(m)
        self.assertEqual(
            match_outcome,
            [
                {u'goals_for': 0, u'won': 0, u'goals_against': 3, u'lost': 1, u'team': home,
                 u'played': 1, u'drew': 0, u'points': 0},
                {u'goals_for': 3, u'won': 1, u'goals_against': 0, u'lost': 0, u'team': away,
                 u'played': 1, u'drew': 0, u'points': 3}
            ])

    def test_teams_standings(self):
        teams, matches = self.__gen_matches__()
        league = League(u'Süper Lig')

        for m in matches:
            league.add_match(m)

        standings = league.get_league_table
        self.assertEqual(
            standings,
            [
                {u'position': 1, u'points': 14, u'team': u'Ankaragücü'},
                {u'position': 2, u'points': 8, u'team': u'Gençlerbirliği'},
                {u'position': 2, u'points': 8, u'team': u'Kasımpaşa'},
                {u'position': 4, u'points': 2, u'team': u'Feriköy'}
            ]
        )

    def test_no_teams_standings(self):
        l = League(u'League of Sorrow')

        standings = l.get_league_table
        self.assertEqual(standings, [])

    def test_incomplete_standings(self):
        l = League(u'Lega Procrastica')
        home = Team(u'Anubis Incompeta')
        away = Team(u'Doitus Latero')
        m = Match(home, 0, away, 0)
        l.add_match(m)

        standings = l.get_league_table
        self.assertEqual(
            standings,
            [
                {u'points': 1, u'position': 1, u'team': u'Anubis Incompeta'},
                {u'points': 1, u'position': 1, u'team': u'Doitus Latero'},
            ]
        )

if __name__ == u'__main__':
    unittest.main()
