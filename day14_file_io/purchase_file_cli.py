def load_purchases(filename):
    purchases = []

    with open(filename) as texts:
        for text in texts:
            text = text.strip()
            parts = text.split(",")

            category = parts[0]
            amount = int(parts[1])
            purchases.append((category, amount))

    return purchases


purchases = load_purchases("purchases.txt")
print(purchases)