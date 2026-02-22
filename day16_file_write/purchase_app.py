def load_purchases(filename):
    purchases = []

    try:
        with open(filename) as texts:
            for text in texts:
                text = text.strip()
                parts = text.split(",")

                category = parts[0]

                try:
                    amount = int(parts[1])
                    purchases.append((category, amount))
                except ValueError:
                    print(f"Skipping invalid line: {text}")
    
    except FileNotFoundError:
        print("File not found")
        return purchases
    
    return purchases

def main():
    purchases = load_purchases("purchases.txt")

    while True:
        print("\nMenu")
        print("1. Show totals")
        print("2. Show highest category")
        print("3. Show categories above threshold")
        print("4. Add purchase")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(show_totals(purchases))
        elif choice == "2":
            print(show_highest_category(purchases))
        elif choice == "3":
            while True:
                try:
                    threshold = int(input("Threshold?: "))
                    break                    
                except ValueError:
                    print("Enter a valid number")
                
            print(show_category_above(purchases, threshold))
        
        elif choice == "4":
            add_purchase("purchases.txt", purchases)

        elif choice == "5":
            break
        else:
            print("Invalid choice")
        
def total_by_category(purchases):
    totals = {}
    for category, amount in purchases:
        totals[category] = totals.get(category, 0) + amount
    return totals

def show_totals(purchases):
    return total_by_category(purchases)

def show_highest_category(purchases):
    totals = total_by_category(purchases)
    if not totals:
        return "No data"
    
    return max(totals, key=totals.get)

def show_category_above(purchases, threshold):
    totals = total_by_category(purchases)
    result = []
    
    for key, value in totals.items():
        if value >= threshold:
            result.append(key)
    
    return result

def add_purchase(filename, purchases):
    category = input("Category: ")
    amount = input("Amount: ")

    try:
        amount = int(amount)
    except ValueError:
        print("Invalid amount")
        return

    # Save to file
    with open(filename, "a") as f:
        f.write(f"{category},{amount}\n")
    
    # Update in-memory list
    purchases.append((category, amount))

    print("Purchase added.")


if __name__ == "__main__":
    main()

