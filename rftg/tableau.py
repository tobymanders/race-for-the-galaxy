

class Tableau:

    def __init__(self, tableau_limit):
        self.tableau = []
        self.tableau_limit = tableau_limit

    def add_to_tableau(self, card):
        # Add card to tableau.
        self.tableau.append(card)

    def print_tableau(self):
        if self.tableau:
            for card in self.tableau:
                print(card)
        else:
            print('Tableau Empty')

    def tableau_complete(self):
        return len(self.tableau) > self.tableau_limit


