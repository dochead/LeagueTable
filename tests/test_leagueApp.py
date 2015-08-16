import unittest

from leaguetable import app

class TestLeagueApp(unittest.TestCase):
    def test_run_file(self):
        a = app.LeagueApp(input_type='file', filename='../samples/results.txt')
        result = a.run()
        self.assertEqual(
            result,
            '\nLeague Table:'
            '1. Tarantulas, 6pts\n'
            '2. Lions, 5pts\n'
            '3. FC Awesome, 1pts\n'
            '3. Snakes, 1pts\n'
            '5. Grouches, 0pts\n'
        )

    def test_run_no_file(self):
        with self.assertRaises(IOError):
            a = app.LeagueApp(input_type='file')


    def test_run_missing_file(self):
        a = app.LeagueApp(input_type='file', filename='missing.txt')
        with self.assertRaises(IOError):
            a.run()
