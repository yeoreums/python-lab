def read_data(filename):
    lines = []

    with open(filename) as file:
        next(file)

        for line in file:
            line = line.strip()
            lines.append(line)
    
    return lines


def parse_rows(lines):
    rows = []

    for line in lines:
        date, product, category, amount = line.split(",")
        rows.append((date, product, category, int(amount)))
    

    return rows


def count_products(rows):
    counts = {}

    for _, product, _, _ in rows:
        counts[product] = counts.get(product, 0) + 1
    
    return counts

def main():
    lines = read_data("sales.csv")
    rows = parse_rows(lines)
    counts = count_products(rows)
    
    max_product = None
    max_count = 0
    for product, count in counts.items():
        if count > max_count:
            max_product = product
            max_count = count

    print(max_product, max_count)

    # Pythonic version using max()
    # product, count = max(counts.items(), key=lambda x: x[1])
    # print(product, count)

if __name__ == "__main__":
    main()
