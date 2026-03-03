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


def group_by_category(rows):
    totals = {}

    for _, _, category, amount in rows:
        totals[category] = totals.get(category, 0) + amount
    

    return totals


def main():
    threshold = 10

    lines = read_data("sales.csv")
    rows = parse_rows(lines)
    totals = group_by_category(rows)

    for category, amount in totals.items():
        if amount > threshold:
            print(category, amount)


if __name__ == "__main__":
    main()