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
    lines = read_data("sales.csv")
    rows = parse_rows(lines)
    totals = group_by_category(rows)

    sorted_items = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    print(sorted_items)
    N = 2
    top_items = sorted_items[:N]
    for category, amount in top_items:
        print(category, amount)

    # # Improved version 1
    # for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True)[:N]:
    #     print(category, amount)

    # # Improved version 2
    # for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True)[:N]:
    #     print(category, amount)

if __name__ == "__main__":
    main()