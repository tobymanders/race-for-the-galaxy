
def consume_any_color(consume_limit, vp_per_resource, card_per_resource, deck, tableau):
    for i in range(0, consume_limit):
        if tableau.any_goods():
            [index, kind] = tableau.locate_goods()
            tableau.burn_good(index)
