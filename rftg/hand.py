

class Hand:
    def __init__(self, deck):
        self.hand = []
        # Create new hand.
        self.new_hand(deck)

    def spending_power(self):
        cash = len(self.hand) - 1
        return cash

    def add_to_hand(self, cards):
        for card in cards:
            self.hand.append(card)

    def remove_from_hand(self, card_index):
        card = self.hand.pop(card_index)
        return card

    def new_hand(self, deck):
        # Create a new hand.
        cards = deck.draw_from_deck(4)
        self.add_to_hand(cards)

    def development_cards(self):
        developments = [card for card in self.hand if card['Class'] == 'DEVELOPMENT']
        return developments

    def settlement_cards(self):
        settlements = [card for card in self.hand if card['Class'] == 'SETTLEMENT']
        return settlements

    def print_hand(self):
        if self.hand:
            for card in self.hand:
                print(card)
        else:
            print('Hand Empty.')


