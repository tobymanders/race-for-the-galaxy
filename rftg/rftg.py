import game_functions as gf
from hand import Hand
from deck import Deck
from tableau import Tableau

# Settings (to be moved to module).
tableau_limit = 6


def run_game():
    # Initialize game, VPs, deck.
    vp_pool = 12

    # Create instance for storing game stats.
    score = 0

    # Create deck, hand, tableau.
    deck = Deck()
    hand = Hand(deck)
    tableau = Tableau(tableau_limit)

    game_end = False

    # Main game loop.
    while game_end is False:

        # Choose action.
        # phase = gf.choose_action()

        # Play phases.
        for phase in range(0, 3):
            gf.play_phase(phase, deck, hand, tableau)

        # # Update stats.
        # gf.update_stats()

        # Check for game end.
        game_end = gf.end_check(tableau)

run_game()