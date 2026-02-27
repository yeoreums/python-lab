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

def group_by_date(rows):
    totals = {}

    for row in rows:
        date = row[0]
        amount = row[3]

        if date not in totals:
            totals[date] = 0
            
        totals[date] += amount

    return totals

def main():
    lines = read_data("sales.csv")
    rows = parse_rows(lines)
    totals = group_by_date(rows)

    for date in sorted(totals):
        print(date, totals[date])


if __name__ == "__main__":
    main()