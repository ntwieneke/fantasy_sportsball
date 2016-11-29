class League:
    def __init__(self, rankings_dict, matchup_list):
        self.outcomes = []
        self.rankings_dict = rankings_dict
        self.matchup_list = matchup_list

    def gen_outcomes(self, rankings_dict=None, matchup_list=None):
        if rankings_dict == None:
            rankings_dict = self.rankings_dict
            matchup_list = self.matchup_list
        try:
            matchup = matchup_list[0]
            for player in matchup:
                new_rank_dict = rankings_dict.copy()
                new_rank_dict[player] += 1
                new_matchup = matchup_list[1:]
                self.gen_outcomes(new_rank_dict, new_matchup)
        except IndexError:
            self.outcomes.append(rankings_dict)

    def get_wins_to_probabilities(self, league_wins_sorted_desc, rank):
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

    def gen_playoff_probs(self, maximum_rank=6):
        self.all_outcomes = {}
        for player in self.rankings_dict.keys():
            self.all_outcomes[player] = 0

        for outcome in self.outcomes:
            sorted_win_totals = sorted(outcome.values(), reverse=True)
            wins_to_probability = self.get_wins_to_probabilities(sorted_win_totals, maximum_rank)

            for player in outcome:
                self.all_outcomes[player] += wins_to_probability[outcome[player]]

        for player in self.all_outcomes:
            self.all_outcomes[player] = float(self.all_outcomes[player]) / float(len(self.outcomes))
        print "Number of possible outcomes: " + str(len(self.outcomes))
        self.all_outcomes

    def display_playoff_probabilities(self):
        sorted_tuples = sorted(self.all_outcomes.items(), key=lambda x: x[1], reverse=True)
        sorted_players = [i[0] for i in sorted_tuples]
        for player in sorted_players:
            print player + ": " + str(round(self.all_outcomes[player]*100, 3)) + '%'


# ================= Core Code =========================
# Given rankings_dict: a dictionary with teams as keys and wincounts as values
# eg: {'nate': 7, 'matt': 6, 'steve': 6,  'addison': 6, 'anton': 6, 'abu': 5, 'anthony': 5, 'mark': 4, 'micah': 4, 'cam': 4, 'joyce': 4, 'taylor': 3}
# Given matchup_list: a list of matchup lists. The matchups lists contain the name of the two teams in mathchup
# eg: [['nate', 'micah'], ['abu', 'steve'], ['taylor', 'joyce'], ['cam', 'mark'], ['matt', 'anthony'], ['anton', 'addison']]
# Also requires an empty list named outcomes to exist
# Returns nothing, instead adds a dictionary to outcomes list. Each dictionary is one of the distinct possible outcomes,
# a changed rankings_dict with assigned winners for each match
# def gen_outcomes(rankings_dict, matchup_list):

# Given list of total wins from each team sorted descending
# eg: [7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 4, 3]
# returns a probability of making it into playoffs based on total wins
# eg: {3: 0, 4: 0, 5: 0, 6: 0.75, 7: 1} 
# def get_wins_to_probabilities(league_wins_sorted_desc):


# # Iterates through every possible outcome
# def playoff_probs(outcomes):

        
# ================= Seed Data =========================

if __name__ == "__main__":
    # Week 10 results
    # rankings_dict = {
    #     'nate': 7,
    #     'matt': 6,
    #     'steve': 6, 
    #     'addison': 6,
    #     'anton': 6,
    #     'abu': 5,
    #     'anthony': 5,
    #     'mark': 4,
    #     'micah': 4,
    #     'cam': 4,
    #     'joyce': 4,
    #     'taylor': 3
    # }

    # Week 11 results
    # rankings_dict = {
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
    rankings_dict = {
        'nate': 8,
        'addison': 8,
        'steve': 7, 
        'anton': 7,
        'matt': 6,
        'anthony': 6,
        'mark': 6,
        'joyce': 6,
        'abu': 5,
        'micah': 5,
        'cam': 4,
        'taylor': 4
    }

    # week_11 = [
    #     ['nate', 'micah'],
    #     ['abu', 'steve'],
    #     ['taylor', 'joyce'],
    #     ['cam', 'mark'],
    #     ['matt', 'anthony'],
    #     ['anton', 'addison']
    # ]

    # week_12 = [
    #     ['nate', 'anton'],
    #     ['abu', 'taylor'],
    #     ['cam', 'joyce'],
    #     ['matt', 'mark'], 
    #     ['micah', 'anthony'],
    #     ['addison', 'steve']
    # ]

    week_13 = [
        ['nate', 'addison'],
        ['abu', 'cam'],
        ['taylor', 'steve'],
        ['matt', 'joyce'],
        ['micah', 'mark'],
        ['anton', 'anthony']
    ]

    # ================= Driver Code =========================

    # my_league = League(rankings_dict, week_11)
    # my_league = League(rankings_dict, week_11 + week_12)
    # my_league = League(rankings_dict, week_11 + week_12 + week_13)

    my_league = League(rankings_dict, week_13)
    my_league.gen_outcomes()
    my_league.gen_playoff_probs(6)
    my_league.display_playoff_probabilities()
    


