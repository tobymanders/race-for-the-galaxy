

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

    def discard_from_hand(self, deck, num):
        for i in range(0, num):
            card = self.remove_from_hand(0)
            deck.add_to_discards(card)

    def new_hand(self, deck):
        # Create a new hand.
        cards = deck.draw_from_deck(4)
        self.add_to_hand(cards)

    def print_hand(self):
        if self.hand:
            for card in self.hand:
                print(card)
        else:
            print('Hand Empty.')

    def cards_in_hand(self):
        return len(self.hand)

    def hand_limit(self, deck):
        n = self.cards_in_hand()
        if n > 10:
            num_to_discard = n - 10
            self.discard_from_hand(deck, num_to_discard)
