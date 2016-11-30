# A League is initialized with:
# Teams_wins: a dictionary with teams as keys and wincounts as values
# eg: {'nate': 7, 'matt': 6, 'steve': 6,  'addison': 6, 'anton': 6, 'abu': 5, 'anthony': 5, 'mark': 4, 'micah': 4, 'cam': 4, 'joyce': 4, 'taylor': 3}
# Matchup_schedule: a list of matchups. An example of a matchup would be ['taylor', 'joyce']
# eg: [['nate', 'micah'], ['abu', 'steve'], ['taylor', 'joyce'], ['cam', 'mark'], ['matt', 'anthony'], ['anton', 'addison']]
class League:
    def __init__(self, teams_wins, matchup_schedule):
        self.possible_outcomes = []
        self.teams_wins = teams_wins
        self.matchup_schedule = matchup_schedule

    # Recursively generates all possible outcomes as teams_wins dictionaries, and appends them to self.possible_outcomes
    # WARNING! This is O(N^2) for N matchups. For a 12 person league with 6 matches a week, each week multiplies calculation time by 64
    def gen_outcomes(self, teams_wins=None, matchup_schedule=None):
        if teams_wins == None:
            teams_wins = self.teams_wins
            matchup_schedule = self.matchup_schedule
        try:
            matchup = matchup_schedule[0]
            for player in matchup:
                new_rank_dict = teams_wins.copy()
                new_rank_dict[player] += 1
                new_matchup = matchup_schedule[1:]
                self.gen_outcomes(new_rank_dict, new_matchup)
        except IndexError:
            self.possible_outcomes.append(teams_wins)

    # Internally called method to 
    # Given list of total wins from each team sorted descending
    # eg: [7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 4, 3]
    # And given lowest rank possible for playoff contention (eg. 6)
    # Returns a probability of making it into playoffs based on total wins
    # eg: {3: 0, 4: 0, 5: 0, 6: 0.75, 7: 1} (only 3 of the 4 people with 6 points would be in the top 6 players and proceed to playoffs)
    def __get_wins_to_probabilities(self, league_wins_sorted_desc, rank):
        result = {}
        initial_index = -1
        current_num = -1
        for i, wins in enumerate(league_wins_sorted_desc):
            if wins != current_num:
                current_num = wins
                initial_index = i
                if i < rank:
                    result[wins] = 1
                else:
                    result[wins] = 0
            else:
                if i < rank:
                    result[wins] = 1
                elif initial_index < rank:
                    result[wins] = float(rank - initial_index) / (i + 1 - initial_index)
                else:
                    result[wins] = 0
        return result

    # Generates the probability of each team reaching the maximum rank
    def gen_playoff_probabilities(self, maximum_rank=6):
        self.probabilities = {}
        for player in self.teams_wins.keys():
            self.probabilities[player] = 0

        # For each outcome, a dictionary of wins to probabilities (of placing maximum_rank or higher) is created.
        # The correlating probability for each team to achieve maximum_rank or better is added to that team in self.probabilities
        for outcome in self.possible_outcomes:
            sorted_win_totals = sorted(outcome.values(), reverse=True)
            wins_to_probability = self.__get_wins_to_probabilities(sorted_win_totals, maximum_rank)

            for player in outcome:
                self.probabilities[player] += wins_to_probability[outcome[player]]

        for player in self.probabilities:
            self.probabilities[player] = float(self.probabilities[player]) / float(len(self.possible_outcomes))

    # Prints probabilities prettily
    def display_playoff_probabilities(self):
        print "Number of possible outcomes: " + str(len(self.possible_outcomes))
        sorted_tuples = sorted(self.probabilities.items(), key=lambda x: x[1], reverse=True)
        sorted_players = [i[0] for i in sorted_tuples]
        for player in sorted_players:
            print player + ": " + str(round(self.probabilities[player]*100, 3)) + '%'

        
# ================= Seed Data and Driver Code =========================

if __name__ == "__main__":
    # Week 10 results
    teams_wins = {
        'nate': 7,
        'matt': 6,
        'steve': 6, 
        'addison': 6,
        'anton': 6,
        'abu': 5,
        'anthony': 5,
        'mark': 4,
        'micah': 4,
        'cam': 4,
        'joyce': 4,
        'taylor': 3
    }

    # Week 11 results
    # teams_wins = {
    #     'nate': 8,
    #     'steve': 7, 
    #     'addison': 7,
    #     'matt': 6,
    #     'anton': 6,
    #     'anthony': 6,
    #     'abu': 5,
    #     'mark': 5,
    #     'joyce': 5,
    #     'micah': 4,
    #     'cam': 4,
    #     'taylor': 3
    # }

    # Week 12 results
    # teams_wins = {
    #     'nate': 8,
    #     'addison': 8,
    #     'steve': 7, 
    #     'anton': 7,
    #     'matt': 6,
    #     'anthony': 6,
    #     'mark': 6,
    #     'joyce': 6,
    #     'abu': 5,
    #     'micah': 5,
    #     'cam': 4,
    #     'taylor': 4
    # }

    week_11 = [
        ['nate', 'micah'],
        ['abu', 'steve'],
        ['taylor', 'joyce'],
        ['cam', 'mark'],
        ['matt', 'anthony'],
        ['anton', 'addison']
    ]

    week_12 = [
        ['nate', 'anton'],
        ['abu', 'taylor'],
        ['cam', 'joyce'],
        ['matt', 'mark'], 
        ['micah', 'anthony'],
        ['addison', 'steve']
    ]

    week_13 = [
        ['nate', 'addison'],
        ['abu', 'cam'],
        ['taylor', 'steve'],
        ['matt', 'joyce'],
        ['micah', 'mark'],
        ['anton', 'anthony']
    ]

    # ================= Driver Code =========================

    # my_league = League(teams_wins, week_11)
    # my_league = League(teams_wins, week_11 + week_12)
    # my_league = League(teams_wins, week_11 + week_12 + week_13)

    my_league = League(teams_wins, week_11 + week_12 + week_13)
    my_league.gen_outcomes()
    my_league.gen_playoff_probabilities(6)
    my_league.display_playoff_probabilities()