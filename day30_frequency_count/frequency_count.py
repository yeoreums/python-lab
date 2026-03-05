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

    for product, count in counts.items():
        print(product, count)


if __name__ == "__main__":
    main()