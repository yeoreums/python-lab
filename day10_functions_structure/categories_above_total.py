def categories_above_total(purchases, threshold):
    result = {}
    r = []
    for category, amount in purchases:
        result[category] = result.get(category, 0) + amount
    
    for key, value in result.items():
        if value >= threshold:
            r.append(key)
    
    return r

purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20),
    ("transport", 15)
]

threshold = 15

print(categories_above_total(purchases, threshold))