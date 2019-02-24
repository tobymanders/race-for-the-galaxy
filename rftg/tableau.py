

class Tableau:

    def __init__(self, tableau_limit):
        self.tableau = []
        self.tableau_limit = tableau_limit

    def add_to_tableau(self, card):
        # Add card to tableau.
        self.tableau.append(card)
        if card['Class'] == 'SETTLEMENT':
            if card['Windfall']:
                self.produce_good(-1)

    def print_tableau(self):
        if self.tableau:
            for card in self.tableau:
                print(card)
        else:
            print('Tableau Empty')

    def tableau_complete(self):
        return len(self.tableau) > self.tableau_limit

    def produce_good(self, index):
        self.tableau[index]['Good'] = 1

    def get_defense(self):
        defense = 0
        for card in self.tableau:
            defense += card['Defense']
        return defense

    # def get_trade_powers(self):
    #
    # def get_consume_powers(self):

    def consume_developments(self):
        cards = []
        for card in self.tableau:
            if card['Phase1'] == 3 or card['Phase2'] == 3:
                cards.append(card)
        return cards




