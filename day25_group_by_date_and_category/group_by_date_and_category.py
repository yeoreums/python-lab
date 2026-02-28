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

def group_by_date(rows):
    totals = {}

    for date, product, category, amount in rows:
        totals[date] = totals.get(date, 0) + amount
    
    return totals

def group_by_category(rows):
    totals = {}

    for _, _, category, amount in rows:
        totals[category] = totals.get(category, 0) + amount

    return totals

def group_by_date_and_category(rows):
    totals = {}

    for date, product, category, amount in rows:
        if date not in totals:
            totals[date] = {}
                
        totals[date][category] = totals[date].get(category, 0) + amount
        # if category not in totals[date]:
        #     totals[date][category] = 0
        
        # totals[date][category] += amount

    return totals
        

def main():
    lines = read_data("sales.csv")
    rows = parse_rows(lines)
    totals = group_by_date_and_category(rows)

    for date in sorted(totals):
        print(date)
        for category, amount in totals[date].items():
            print(" ", category, amount)

if __name__ == "__main__":
    main()