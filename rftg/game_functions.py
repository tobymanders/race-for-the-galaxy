import random


def end_check(tableau):
    ended = tableau.tableau_complete()
    if ended:
        print('GAME COMPLETE.')
        print('Final Tableau:')
        tableau.print_tableau()

    return ended


def choose_discard(cards):
    # Logic for choosing the weakest card.
    discard = cards.pop(0)
    return discard, cards


def choose_discard_from_hand(hand):
    discard = hand.remove_from_hand(0)
    return discard


def affordable_cards(hand, cards):
    spending_power = hand.spending_power()
    affordable = [card for card in cards if card['Cost'] <= spending_power]
    return affordable


def choose_action():
    # For now, choose a random action from the 5 phases.
    return random.randint(0, 4)


def draw_to_hand(num, deck, hand):
    cards = deck.draw_from_deck(num)
    hand.add_to_hand(cards)


def find_index(name, cards):
    """Find index of a card in a set of cards by matching the name."""
    for i, d in enumerate(cards):
        if d['Name'] == name:
            return i


def discard_from_hand(num, deck, hand):
    for i in range(0, num):
        discard = choose_discard_from_hand(hand)
        deck.add_to_discards(discard)


def build(card, deck, hand, tableau):
    # Remove card from hand
    card_ind = find_index(card['Name'], hand.hand)
    hand.remove_from_hand(card_ind)

    # Pay the fee.
    cost = card['Cost']
    discard_from_hand(cost, deck, hand)

    # Add card to tableau.
    tableau.add_to_tableau(card)


def play_phase(phase, deck, hand, tableau):
    if phase == 0:
        explore(deck, hand)
    if phase == 1:
        develop(deck, hand, tableau)
    if phase == 2:
        settle(deck, hand, tableau)
    if phase == 3:
        consumetrade()
    if phase == 4:
        produce()


def explore(deck, hand):
    # Draw from deck, choose discards, add remaining cards to hand.
    # to-do: evaluate tableau and action card for perks
    num_to_draw = 3
    # num_to_discard = 1

    # Draw
    cards = deck.draw_from_deck(num_to_draw)

    # Choose discard
    discard, cards = choose_discard(cards)

    # Discard
    deck.add_to_discards(discard)

    # Add rest to hand
    hand.add_to_hand(cards)


def develop(deck, hand, tableau):
    # List development options from hand.
    dev_cards = hand.development_cards()

    # Just affordable cards.
    affordable = affordable_cards(hand, dev_cards)

    # Choose a development to build (if possible).
    if affordable:

        # For now, choose first affordable card.
        build(affordable[0], deck, hand, tableau)

    # To-do: tally perks and apply.


def settle(deck, hand, tableau):
    # List settlement options from hand.
    set_cards = hand.settlement_cards()

    # Just affordable cards.
    affordable = affordable_cards(hand, set_cards)

    # Choose a development to build (if possible).
    if affordable:
        # For now, choose first affordable card.
        build(affordable[0], deck, hand, tableau)

    # To-do: tally perks and apply.

def consumetrade():


    # To do
    print('Not yet implemented.')


def produce():
    # To do
    print('Not yet implemented.')
