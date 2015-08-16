# -*- coding: utf-8 -*-.

import unittest

from leaguetable.team import Team


class TestTeam(unittest.TestCase):
    def test_team_define(self):
        t = Team(u'Liddlypool')
        self.assertEqual(unicode(t), u'Liddlypool')

    def test_match_international(self):
        away = Team(u'Александра')
        self.assertEqual(away.team_name, u'Александра')


if __name__ == u'__main__':
    unittest.main()
