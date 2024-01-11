

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
            'K': 70,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 20,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 17,
            'Y': 20,
            'Z': 21
            }

    special_offers = {
         'A': [(5, 200), (3, 130)], 
         'B': [(2, 45)], 
         'H': [(10, 80), (5, 45)],
         'K': [(2, 120)],
         'P': [(5, 200)],
         'Q': [(3, 80)],
         'V': [(3, 130), (2, 90)]
        }

    if not all(sku in prices for sku in skus):
        return -1
    
    total = 0
    items_count = {item: skus.count(item) for item in set(skus)}

    free_items = [('E', 'B'), ('N', 'M'), ('R', 'Q'), ('F', 'F'), ('U', 'U')]
    quantity_needed = {'E': 2, 'N': 3, 'R': 3, 'F': 3, 'U': 4}
    for paid_item, free_item in free_items:
        free_item_count = items_count.get(paid_item, 0) // quantity_needed[paid_item]
        items_count[free_item] = max(0, items_count.get(free_item, 0) - free_item_count)

    group_offer_price = 45
    group_offer_items = 'STXYZ'
    group_offer_count = sum(items_count.get(item, 0) for item in group_offer_items)
    group_offer_set = group_offer_count // 3
    if group_offer_set > 0:
        group_items_sorted = sorted(group_offer_items, key=lambda x: prices[x])
        for _ in range(group_offer_set):
            for item in group_items_sorted:
                if items_count[item] > 0:
                    items_count[item] -= 1
                    group_offer_count -= 1
                    if group_offer_count % 3 == 0:
                        break
        #total += group_offer_set * group_offer_price
    

    for item, offers in special_offers.items():
        for offer_quantity, offer_price in offers:
            while items_count.get(item, 0) >= offer_quantity:
                total += offer_price
                items_count[item] -= offer_quantity
    

    for item, count in items_count.items():
            total += count * prices[item]

    return total





