def total_spent_above_limit(purchases, limit):
    result = {}

    for c, a in purchases:
        if a >= limit:
            result[c] = result.get(c, 0) + a

    return result

purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20)
]

limit = 8

print(total_spent_above_limit(purchases, limit))