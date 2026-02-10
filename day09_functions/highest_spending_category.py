def highest_spending_category(purchases):
    t = {}
    for c, a in purchases:
        t[c] = t.get(c, 0) + a
    
    if not t:
        return None

    return max(t, key=t.get)



purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20)
]

print(highest_spending_category(purchases))