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

    def get_vp_total(self, tableau):
        vp_total = self.count_vp(tableau) + self.get_player_vp()
        return vp_total

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
        name = card['Name']
        if name == 'NEW ECONOMY':
            consume_cards = gf.consume_cards(tableau.tableau)
            for card in gf.development_cards(consume_cards):
                vp_total += 2
            for card in gf.settlement_cards(consume_cards):
                vp_total += 1
        elif name == 'MINING LEAGUE':
            for card in gf.settlement_cards(tableau.tableau):
                if card['Kind'] == 'rare' and card['Windfall'] == 0:
                    vp_total += 2
                elif card['Kind'] == 'rare' and card['Windfall'] == 1:
                    vp_total += 1
            for card in gf.development_cards(tableau.tableau):
                if name == 'MINING ROBOTS' or name == 'MINING CONGLOMERATE':
                    vp_total += 2
        elif name == 'FREE TRADE ASSOCIATION':
            for card in gf.settlement_cards(tableau.tableau):
                if card['Kind'] == 'novelty' and card['Windfall'] == 0:
                    vp_total += 2
                elif card['Kind'] == 'novelty' and card['Windfall'] == 1:
                    vp_total += 1
            for card in gf.development_cards(tableau.tableau):
                if name == 'CONSUMER MARKETS' or name == 'EXPANDING COLONY':
                    vp_total += 2
        elif name == 'TRADE LEAGUE':
            trade_cards = gf.trade_cards(tableau.tableau)
            for card in gf.development_cards(trade_cards):
                vp_total += 2
            for card in gf.settlement_cards(trade_cards):
                vp_total += 1
        elif name == 'MERCHANT GUILD':
            for card in gf.settlement_cards(tableau.tableau):
                if 'Kind' in card and card['Windfall'] == 0:
                    vp_total += 2
        elif name == 'GALACTIC IMPERIUM':
            for card in gf.settlement_cards(tableau.tableau):
                if 'REBEL' in card['Name']:
                    vp_total += 2
                elif card['Type'] == 'M':
                    vp_total += 1
        elif name == 'GALACTIC FEDERATION':
            for card in gf.development_cards(tableau.tableau):
                if card['Cost'] == 6:
                    vp_total += 2
                else:
                    vp_total += 1
        elif name == 'NEW GALACTIC ORDER':
            vp_total += tableau.get_defense()
        elif name == 'PAN-GALACTIC LEAGUE':
            for card in gf.settlement_cards(tableau.tableau):
                if card['Kind'] == 'genes':
                    vp_total += 2
                elif card['Type'] == 'M':
                    vp_total += 1
            for card in gf.development_cards(tableau.tableau):
                if name == 'CONTACT SPECIALIST':
                    vp_total += 3
        elif name == 'ALIEN TECH INSTITUTE':
            for card in gf.settlement_cards(tableau.tableau):
                if card['Kind'] == 'alien' and card['Windfall'] == 0:
                    vp_total += 3
                elif card['Kind'] == 'alien' and card['Windfall'] == 1:
                    vp_total += 2
                elif 'ALIEN' in card['Name']:
                    vp_total += 2

        return vp_total