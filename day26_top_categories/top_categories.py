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

    # print(sorted(totals.items()))   # for debugging

    # Step by step to understand the concept
    sorted_items = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    print(sorted_items)
    for category, amount in sorted_items:
        print(category, amount)

    # Shorter version
    # for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):        
    #     print(category, amount)

    
    # Mental model to understand better
    '''
    totals = {'Fruit': 9, 'Dairy': 12}

    totals.items()
    → [('Fruit', 9), ('Dairy', 12)]

    sorted(...)
    → [('Dairy', 12), ('Fruit', 9)]

    for category, amount in ...
    → unpack each tuple
    '''


if __name__ == "__main__":
    main()