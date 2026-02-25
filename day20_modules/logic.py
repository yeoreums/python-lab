def total_by_category(purchases):
    totals = {}
    for category, amount in purchases:
        totals[category] = totals.get(category, 0) + amount
    return totals

def show_totals(purchases):
    return total_by_category(purchases)

def show_highest_category(purchases):
    totals = total_by_category(purchases)
    if not totals:
        return "No data"
    
    return max(totals, key=totals.get)

def show_category_above(purchases, threshold):
    totals = total_by_category(purchases)
    result = []
    
    for key, value in totals.items():
        if value >= threshold:
            result.append(key)
    
    return result

def show_all_purchases(purchases):
    if not purchases:
        print("No purchases found")
        return

    for i, (category, amount) in enumerate(purchases, start=1):
        print(i, category, amount)