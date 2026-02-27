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
        parts = line.split(",")

        date = parts[0]
        product = parts[1]
        category = parts[2]
        amount = int(parts[3])

        rows.append((date, product, category, amount))

    return rows

def group_by_category(rows):
    totals = {}

    for row in rows:
        category = row[2]
        amount = row[3]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    return totals

def main():
    lines = read_data("sales.csv")
    rows = parse_rows(lines)
    totals = group_by_category(rows)

    for category in totals:
        print(category, totals[category])


if __name__ == "__main__":
    main()