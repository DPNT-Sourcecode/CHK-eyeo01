

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}

    special_offers = {
         'A': [(5, 200), (3, 130)], 
         'B': [(2, 45)], 
         'F': [(3, 20)]
         }

    if not all(sku in prices for sku in skus):
        return -1
    
    total = 0
    items_count = {item: skus.count(item) for item in set(skus)}

    free_b = items_count.get('E', 0) // 2
    items_count['B'] = max(0, items_count.get('B', 0) - free_b)

    for item, offers in special_offers.items():
        for offer_quantity, offer_price in offers:
            while items_count.get(item, 0) >= offer_quantity:
                total += offer_price
                items_count[item] -= offer_quantity
    

    for item, count in items_count.items():
            total += count * prices[item]

    return total


