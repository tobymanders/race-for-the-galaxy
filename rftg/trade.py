from operator import itemgetter

class Trade:
    def __init__(self):
        self.base_trade_rates = {'novelty': 2, 'rare': 3,
                            'genes': 4, 'alien': 5}

        self.trade_rates = self.base_trade_rates

        self.card_modifiers = {'DISTANT WORLD': ('novelty', 3),
                               'BIO-HAZARD MINING WORLD': ('genes', 2),
                               'SPACE PORT': ('rare', 2),
                               'SPICE WORLD': ('novelty', 2),
                               'MERCHANT WORLD': ('any', 2),
                               'EXPORT DUTIES': ('any', 1),
                               'GENETICS LAB': ('genes', 1),
                               'MINING CONGLOMERATE': ('rare', 1),
                               'TRADE LEAGUE': ('any', 1),
                               }
        # TODO: implement trade perks for just that world's good.
        # PIRATE WORLD

    def modify_trade_rate(self, color, modifier):
        self.trade_rates[color] += modifier

    def get_trade_value(self, card):
        value = self.trade_rates[card['Kind']]
        return value

    def update_trade_rates(self, tableau):
        # TODO: call this function before any trade turn.
        self.trade_rates
        for card in tableau.tableau:
            name = card['Name']
            if name in self.card_modifiers:
                kind, modifier = self.card_modifiers[name]
                if kind is not 'any':
                    self.trade_rates[kind] += modifier
                else:
                    for k in self.trade_rates:
                        self.trade_rates[k] += modifier

    def trade(self, deck, hand, tableau, trade):
        goods = tableau.find_goods(trade)
        if goods:
            [ind, val, kind] = max(goods, key=itemgetter(1))
            print("Trading %s good for %d cards." % (kind, val))
            tableau.burn_good(ind)
            deck.draw_to_hand(hand, val)
