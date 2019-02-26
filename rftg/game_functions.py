import random


def end_check(tableau, scoreboard):
    ended = False
    ended_tableau = tableau.tableau_complete()
    ended_vp = scoreboard.vp_pool_exhausted()

    if ended_tableau or ended_vp:
        ended = True

        print('GAME COMPLETE.')
        print('Final Tableau:')
        tableau.print_tableau()

        vp_total = scoreboard.count_vp(tableau) + scoreboard.get_player_vp()
        print('Final VPs:', vp_total)

    return ended


def choose_discard(cards):
    # Logic for choosing the weakest card.
    discard = cards.pop(0)
    return discard, cards


def choose_discard_from_hand(hand):
    discard = hand.remove_from_hand(0)
    return discard


def development_cards(cards):
    developments = [card for card in cards if card['Class'] == 'DEVELOPMENT']
    return developments


def settlement_cards(cards):
    settlements = [card for card in cards if card['Class'] == 'SETTLEMENT']
    return settlements


def affordable_cards(hand, cards, tableau, card_type):
    """card_type is 1 for settlements, 0 for developments"""
    spending_power = hand.spending_power()
    defense = tableau.get_defense()
    if card_type == 1:
        affordable = [card for card in cards if (card['Cost'] <= spending_power and card['Type'] == 'C')
                        or (card['Cost'] <= defense and card['Type'] == 'M')]
    else:
        affordable = [card for card in cards if card['Cost'] <= spending_power]
    return affordable


def consume_cards(cards):
    subset = []
    for card in cards:
        if 3 in card['Phase']:
            subset.append(card)
    return subset


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
    if card['Class'] == 'SETTLEMENT':
        if card['Type'] == 'C':
            cost = card['Cost']
            discard_from_hand(cost, deck, hand)
    else:
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
        consume_trade(deck, hand, tableau)
    if phase == 4:
        produce(tableau)


def explore(deck, hand):
    # Draw from deck, choose discards, add remaining cards to hand.
    # TODO: evaluate tableau and action card for perks
    # TODO: account for two explore cards
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
    dev_cards = development_cards(hand.hand)

    # Just affordable cards.
    affordable = affordable_cards(hand, dev_cards, tableau, 0)

    # Choose a development to build (if possible).
    if affordable:

        # For now, choose first affordable card.
        build(affordable[0], deck, hand, tableau)

    # TODO: tally perks and apply.


def settle(deck, hand, tableau):
    # List settlement options from hand.
    set_cards = settlement_cards(hand.hand)

    # Just affordable cards.
    affordable = affordable_cards(hand, set_cards, tableau, 1)

    # Choose a development to build (if possible).
    if affordable:
        # For now, choose first affordable card.
        build(affordable[0], deck, hand, tableau)

    # To-do: tally perks and apply.


def play_trade(tableau):
    tableau.use_trade_powers(hand)


def consume_trade(deck, hand, tableau):
    # For now, always play trade.
    play_trade(tableau)

    # List of consume powers
    tableau.use_consume_powers()


def produce(tableau):
    # TODO: account for hand bonus perks
    for ind, card in enumerate(tableau.tableau):
        if card['Class'] is 'SETTLEMENT':
            if card['Windfall'] == 0 and card['Kind']:
                tableau.produce_good(ind)

