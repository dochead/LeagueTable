# -*- coding: utf-8 -*-.

import unittest

from leaguetable.team import Team


class TestTeam(unittest.TestCase):
    def test_team_define(self):
        t = Team(u'Liddlypool')
        self.assertEqual(unicode(t), u'Liddlypool - Pl: 0, W: 0, L: 0, D:0, GF: 0, GA: 0, GD: 0')

    def test_match_international(self):
        away = Team(u'Александра')
        self.assertEqual(away.team_name, u'Александра')


if __name__ == '__main__':
    unittest.main()
