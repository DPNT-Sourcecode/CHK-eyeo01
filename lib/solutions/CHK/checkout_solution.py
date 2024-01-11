

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    special_offers = {'A': (3, 130), 'B': (2, 45)}

    if not all(sku in prices for sku in skus):
        return -1
    
    total = 0
    for item, price in prices.items():
        count = skus.count(item)
        if item in special_offers:
            offer_count, offer_price = special_offers[item]
            total += (count // offer_count) * offer_price
            total += (count % offer_count) * price
        else:
            total += count * price
    



