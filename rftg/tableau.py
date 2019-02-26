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

    def get_defense(self):
        defense = 0
        for card in self.tableau:
            defense += card['Defense']
        return defense

    # def use_trade_powers(self, hand):
    #     for card in self.tableau:
    #         if 5 in card['Phase']:
    #             # TODO: handle trade perks:
    #             # bonus for resource from given card
    #             # bonus for color resource
    #             # bonus for any resource



    def total_goods(self):
        total = 0
        for card in self.tableau:
            if card['Class'] == 'SETTLEMENT':
                total += card['Good']
        return total

    def produce_good(self, index):
        self.tableau[index]['Good'] = 1

    def consume_good(self, kind, vp_per_good, cards_per_good, hand, scoreboard):
        for card in self.tableau:
            if card['Class'] == 'SETTLEMENT' and card['Good'] == 1:
                if kind == card['Kind'] or kind == 'any':
                    card['Good'] == 0
                    scoreboard.add_vp(vp_per_good)
                    hand.draw_to_hand(hand, cards_per_good)

    def use_consume_powers(self):
        for card in self.tableau:
            if 3 in card['Phase'] and self.total_goods > 0:
                self.consume_good((card['Kind'], card['Consume Power']))





