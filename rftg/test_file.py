from deck import Deck
from hand import Hand


deck = Deck()
hand = Hand(deck)

print('DECK:', len(deck.deck))
for card in deck.deck:
    print(card)

print('HAND:', len(hand.hand))
for card in hand.hand:
    print(card)

print('Done')