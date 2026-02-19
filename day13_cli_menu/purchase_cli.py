def main():
    while True:
        print("\nMenu")
        print("1. Show totals")
        print("2. Show highest category")
        print("3. Show categories above threshold")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(show_totals(purchases))
        elif choice == "2":
            print(show_highest_category(purchases))
        elif choice == "3":
            threshold = int(input("Threshold?: "))
            print(show_category_above(purchases, threshold))
        elif choice == "4":
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
    
    return max(totals, key=totals.get)

def show_category_above(purchases, threshold):
    totals = total_by_category(purchases)
    result = []
    
    for key, value in totals.items():
        if value >= threshold:
            result.append(key)
    
    return result


purchases = [
    ("food", 10),
    ("transport", 5),
    ("food", 7),
    ("entertainment", 20),
    ("transport", 15)
]


if __name__ == "__main__":
    main()