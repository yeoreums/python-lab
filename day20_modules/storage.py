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

def delete_purchases(filename, purchases):
    if not purchases:
        print("No purchases to delete")
        return
    
    for i, (category, amount) in enumerate(purchases, start=1):        
        print(i, category, amount)

    while True:
        try:
            num = int(input("Number to delete?: "))
            # Better version: if 1<= num <= len(purchases): 
            if num >= 1 and num <= len(purchases):
                break
            else:
                print("Invalid number")
                continue
        except ValueError:
            print("Enter a valid number")
    
    index = num - 1
    removed = purchases.pop(index)
    print("Deleted:",removed)
        
    with open(filename, "w") as f:
        for category, amount in purchases:
            f.write(f"{category},{amount}\n")

def edit_purchase(filename, purchases):
    if not purchases:
        print("No purchases to edit")
        return

    for i, (category, amount) in enumerate(purchases, start=1):
        print(i, category, amount)
    
    while True:
        try:
            num = int(input("Number to edit?: "))
            if 1 <= num <= len(purchases):
                break
            else:
                print("Invalid number")
        except ValueError:
            print("Enter a valid number")
        
    index = num - 1
    new_category = input("New category: ")

    while True:
        try:
            new_amount = int(input("New amount: "))
            break
        except ValueError:
            print("Enter a valid number")

    purchases[index] = (new_category, new_amount)


    with open(filename, "w") as f:
        for category, amount in purchases:
            f.write(f"{category},{amount}\n")

    print("Purchase updated.")
