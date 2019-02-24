import game_functions as gf

class Scoreboard:

    def __init__(self, vp_pool):
        self.vp_count = 0
        self.vp_pool = vp_pool

    def get_vps_left(self):
        return self.vp_pool

    def vp_pool_exhausted(self):
        return self.vp_pool < 1

    def get_player_vp(self):
        return self.vp_count

    def add_vp(self, num):
        self.vp_count += num
        self.vp_pool -= num

    def count_vp(self, tableau):
        vp_tally = 0
        for card in tableau.tableau:
            vp_tally += card['VP']
            if card['Class'] is 'DEVELOPMENT':
                if card['?']:
                    vp_tally += self.count_six_card(card, tableau)
        return vp_tally

    def count_six_card(self, card, tableau):
        vp_total = 0
        if card['Name'] == 'NEW ECONOMY':
            consume_cards = gf.consume_cards(tableau.tableau)
            for card in gf.development_cards(consume_cards):
                vp_total += 2
            for card in gf.settlement_cards(consume_cards):
                vp_total += 1
            return vp_total