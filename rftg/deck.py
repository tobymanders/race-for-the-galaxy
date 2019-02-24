import csv
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.discards = []

        self.load_settlements()
        self.load_developments()

        self.shuffle()

    def print_deck(self):
        for card in self.deck:
            print(card)

    def print_discards(self):
        for card in self.discards:
            print(card)

    def load_settlements(self):
        with open('settlements.csv') as csvfile:
            f = csv.DictReader(csvfile)
            for row in f:
                new_card = {k: v for k, v in row.items()}
                new_card['Class'] = 'SETTLEMENT'
                new_card['Cost'] = int(new_card['Cost'])
                new_card['VP'] = int(new_card['VP'])
                new_card['Windfall'] = bool(int(new_card['Windfall']))
                new_card['Defense'] = int(new_card['Defense'])
                new_card['Good'] = 0

                self.deck.append(new_card)

    def load_developments(self):
        with open('developments.csv') as csvfile:
            f = csv.DictReader(csvfile)
            for row in f:
                new_card = {k: v for k, v in row.items()}
                new_card['Class'] = 'DEVELOPMENT'
                new_card['Cost'] = int(new_card['Cost'])
                new_card['VP'] = int(new_card['VP'])
                new_card['Defense'] = int(new_card['Defense'])

                self.deck.append(new_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_from_deck(self, num):
        cards = []
        for i in range(0, num):
            if self.deck_empty():
                self.discards_to_deck()
            card = self.deck.pop()
            cards.append(card)
        return cards

    def add_to_discards(self, card):
        self.discards.append(card)
        # print('discards:', self.discards)

    def discards_to_deck(self):
        self.deck = self.discards
        self.discards = []
        self.shuffle()

    def deck_empty(self):
        return len(self.deck) == 0



