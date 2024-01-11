

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
         'H': [(10, 80), (5, 45)],
         'K': [(2, 150)],
         'P': [(5, 200)],
         'Q': [(3, 80)],
         'U': [(3, 80)],
         'V': [(3, 130), (2, 90)]
         }

    if not all(sku in prices for sku in skus):
        return -1
    
    total = 0
    items_count = {item: skus.count(item) for item in set(skus)}

    free_items = [('E', 'B'), ('N', 'M'), ('R', 'Q')]
    
    for paid_item, free_item in free_items:
        free_item_count = items_count.get(paid_item, 0) // 
        items_count[free_item] = max(0, items_count.get(free_item, 0) - free_item_count)

    for item, offers in special_offers.items():
        for offer_quantity, offer_price in offers:
            while items_count.get(item, 0) >= offer_quantity:
                total += offer_price
                items_count[item] -= offer_quantity
    

    for item, count in items_count.items():
            total += count * prices[item]

    return total