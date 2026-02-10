def total_spent_by_category(purchases):
    result = {}

    for c, a in purchases:
        result[c] = result.get(c, 0) + a
    return result


purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20)
]

print(total_spent_by_category(purchases))