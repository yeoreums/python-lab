from storage import load_purchases, add_purchase, delete_purchases, edit_purchase
from logic import show_totals, show_highest_category, show_category_above, show_all_purchases

def main():
    purchases = load_purchases("purchases.txt")

    while True:
        print("\nMenu")
        print("1. Show totals")
        print("2. Show highest category")
        print("3. Show categories above threshold")
        print("4. Add purchase")
        print("5. Delete purchases")
        print("6. Edit purchases")
        print("7. Show all purchases")
        print("8. Exit")        

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
            delete_purchases("purchases.txt", purchases)

        elif choice == "6":
            edit_purchase("purchases.txt", purchases)

        elif choice == "7":
            show_all_purchases(purchases)

        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
