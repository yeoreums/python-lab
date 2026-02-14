def average_spent_per_category(purchases):
    totals = {}
    count = {}
    result = {}

    for category, price in purchases:
        totals[category] = totals.get(category, 0) + price
        count[category] = count.get(category, 0) + 1
    
    for category in totals:
        result[category] = totals[category] / count[category]
    
    return result


purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20),
    ("transport", 15)
]

print(average_spent_per_category(purchases))