import game_functions as gf
from hand import Hand
from deck import Deck
from tableau import Tableau
from scoreboard import Scoreboard
# from settings import Settings

# Settings (to be moved to module).
tableau_limit = 10
vp_pool = 12

# Create scoreboard
scoreboard = Scoreboard(vp_pool)

def run_game():

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

        # Check hand limit
        hand.hand_limit(deck)

        # Check for game end.
        game_end = gf.end_check(tableau, scoreboard)

run_game()