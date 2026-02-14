def total_by_category(purchases):
    totals = {}
    
    for category, amount in purchases:
        totals[category] = totals.get(category, 0) + amount
    
    return totals

def highest_category(purchases):
    result = {}
    
    for category, amount in purchases:
        result[category] = result.get(category, 0) + amount

    return max(result, key=result.get)

def category_above(purchases, threshold):
    totals = {}
    result = []

    for category, amount in purchases:
        totals[category] = totals.get(category, 0) + amount
    
    for key, value in totals.items():
        if value >= threshold:
            result.append(key)
    
    return result


def show_summary(purchases, threshold):
    return (
        f"Totals: {total_by_category(purchases)}\n"
        f"Highest: {highest_category(purchases)}\n"
        f"Above 10: {category_above(purchases, threshold)}"
    )


purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20),
    ("transport", 15)
]

threshold = 10

print(show_summary(purchases, threshold))