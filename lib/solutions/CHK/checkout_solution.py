

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

    special_offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)]}

    if not all(sku in prices for sku in skus):
        return -1
    
    total = 0
    items_count = {item: skus.count(item) for item in set(skus)}
    for item, offers in special_offers.items():
        for offer_quantity, offer_price in offers:
            while items_count[item] >= offer_quantity:
                total += offer_price
                items_count[item] -= offer_quantity
    
    free_b = items_count['E'] // 2
    items_count['B'] = max(0, items_count['B'] - free_b)
    


    for item, price in prices.items():
        count = skus.count(item)
        if item in special_offers:
            offer_count, offer_price = special_offers[item]
            total += (count // offer_count) * offer_price
            total += (count % offer_count) * price
        else:
            total += count * price
    return total



