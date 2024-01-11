

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 
            'B': 30,
            'C': 20,
            'D': 15, 
            'E': 40, 
            'F': 10,
            'G': 20,
            'H': 10,
            'I': 35,
            'J': 60,
            'K': 80,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 30,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 90,
            'Y': 10,
            'Z': 50
            }

    special_offers = {
         'A': [(5, 200), (3, 130)], 
         'B': [(2, 45)], 
         'F': [(3, 20)],
         'H': [()]
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
