def highest_category_above_limit(purchases, limit):
    result = {}

    for c, n in purchases:
        if n >= limit:
            result[c] = result.get(c, 0) + n

    if not result:
        return None
    
    return max(result, key=result.get)


purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20),
    ("transport", 15)
]

limit = 8

print(highest_category_above_limit(purchases, limit))