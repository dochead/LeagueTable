import unittest

from leaguetable import app


class TestLeagueApp(unittest.TestCase):
    def test_run_file(self):
        a = app.LeagueApp(input_type=u'file', filename='../samples/results.txt')
        result = a.run()
        self.assertEqual(
            result,
            u'\nLeague Table:\n\n'
            u'1. Tarantulas, 6pts\n'
            u'2. Lions, 5pts\n'
            u'3. FC Awesome, 1pts\n'
            u'3. Snakes, 1pts\n'
            u'5. Grouches, 0pts\n'
        )

    def test_run_no_file(self):
        with self.assertRaises(IOError):
            app.LeagueApp(input_type=u'file')

    def test_run_missing_file(self):
        a = app.LeagueApp(input_type=u'file', filename='missing.txt')
        with self.assertRaises(IOError):
            a.run()

if __name__ == u'__main__':
    unittest.main()
