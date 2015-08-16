from operator import itemgetter


class League(object):
    def __init__(self, league_name, win_points=3, draw_points=1, lost_points=0):
        """
        League model object takes a name and result points. It provides a way to add
        matches (calculating the stats as it goes), a way to re-calculate stats, get the
        teams added to the league so far and output the league table.

        :param league_name:
        :param win_points:
        :param draw_points:
        :param lost_points:
        """
        self.league_name = league_name
        self.matches = []
        self.won_points = win_points
        self.drew_points = draw_points
        self.lost_points = lost_points

        self._teams = {}
        self._team_types = (u'home', u'away')
        self._update_attrs = [
            u'played',
            u'won',
            u'drew',
            u'lost',
            u'goals_for',
            u'goals_against',
            u'points',
        ]
        self.display_attrs = [
            u'points',
        ]

    def add_match(self, match):
        """
        Takes a match object and adds it to the league structure, in doing so keeps it stored
        in a list for future reference and updates the stats tally.

        :param match:
        """
        for t in self._team_types:
            team_obj = getattr(match, u'{}_team'.format(t))
            if team_obj.team_name not in self._teams:
                self._teams[team_obj.team_name] = {
                    attr: 0 for attr in self._update_attrs
                    }
                self._teams[team_obj.team_name][u'team'] = team_obj

        team_stats = self.__calc_league_stats__(match)
        self.__update_table__(team_stats)

        self.matches.append(match)
        return True

    def __calc_league_stats__(self, match):
        """
        Internal function that generates a lambda to apply to the league as a result of the match
        provided.

        :param match:
        :return: League result dictionary
        """
        result = match.result
        league_result = []
        for i, team in enumerate(self._team_types):
            this_team = u'{}_team'.format(team)
            other_score = u'{}_score'.format(self._team_types[int(not (bool(i)))])
            league_result.append({
                u'team': getattr(match, this_team),
                u'played': 1,
                u'won': 1 if result[team] == u'won' else 0,
                u'drew': 1 if result[team] == u'drew' else 0,
                u'lost': 1 if result[team] == u'lost' else 0,
                u'goals_for': getattr(match, u'{}_score'.format(team)),
                u'goals_against': getattr(match, other_score),
                u'points': getattr(self, u'{}_points'.format(result[team]))
            })

        return league_result

    def __update_table__(self, team_stats):
        for stat in team_stats:
            for attr in self._update_attrs:
                self._teams[stat[u'team'].team_name][attr] += stat[attr]

    @property
    def get_league_table(self):
        """
        Generates a sorted list of dictionaries with teams in league position. Filters out attributes
        that aren't in a list of specified display attributes.

        :return:
        """
        sorted_table = sorted(self._teams.values(), key=itemgetter(u'points', u'team'), reverse=True)
        display_table = []
        display_position = previous_points = -1
        for i, team in enumerate(sorted_table, start=1):
            if previous_points != team[u'points']:
                display_position = i
            row = {
                u'position': display_position,
                u'team': team[u'team'].team_name
            }
            previous_points = team[u'points']
            row.update(
                {stat: team[stat] for stat in self.display_attrs}
            )
            display_table.append(row)
        return display_table

    @property
    def teams(self):
        return self._teams
