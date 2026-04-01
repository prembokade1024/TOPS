from utils import load_data, save_data, log_transaction

def manager_menu():
    """Displays the Manager menu and handles routing."""
    while True:
        print("\n--- Fruit Manager Menu ---")
        print("1. Add Fruit Stock")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        print("4. Return to Main Menu")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_fruit()
        elif choice == '2':
            view_fruits()
        elif choice == '3':
            update_fruit()
        elif choice == '4':
            break
        else:
            print("Invalid input! Please enter a number between 1 and 4.")

def add_fruit():
    """Business Logic: Add new fruit to the stock dictionary."""
    stock = load_data()
    
    while True:
        fruit_name = input("Enter Fruit Name: ").strip().title()
        if not fruit_name.isalpha():
            print("Invalid input! Fruit name must contain only letters.")
            continue
            
        try:
            qty = int(input(f"Enter quantity (in kg) for {fruit_name}: "))
            price = float(input(f"Enter price per kg for {fruit_name}: "))
            
            if qty < 0 or price < 0:
                print("Quantity and Price cannot be negative.")
                continue
                
            # Dictionary manipulation
            if fruit_name in stock:
                stock[fruit_name]['qty'] += qty
                stock[fruit_name]['price'] = price # Update to latest price
            else:
                stock[fruit_name] = {'qty': qty, 'price': price}
                
            save_data(stock)
            msg = f"Manager added {qty}kg of {fruit_name} at ${price:.2f}/kg."
            print(f"\nSuccess: {msg}")
            log_transaction(msg)
            break
            
        except ValueError:
            print("Unexpected input! Please enter valid numeric values for quantity and price.")

def view_fruits():
    """Business Logic: Display all current stock."""
    stock = load_data()
    if not stock:
        print("\nStock is currently empty.")
        return
        
    print("\n--- Current Fruit Stock ---")
    print(f"{'Fruit Name':<15} | {'Quantity (kg)':<15} | {'Price/kg':<10}")
    print("-" * 45)
    for fruit, details in stock.items():
        print(f"{fruit:<15} | {details['qty']:<15} | ${details['price']:<10.2f}")

def update_fruit():
    """Business Logic: Update existing fruit quantity or price."""
    stock = load_data()
    view_fruits()
    
    if not stock:
        return
        
    fruit_name = input("\nEnter the name of the fruit to update: ").strip().title()
    
    if fruit_name not in stock:
        print(f"Error: {fruit_name} is not in the stock. Please 'Add' it first.")
        return
        
    try:
        print("Leave blank to keep current value.")
        new_qty_str = input(f"Enter new total quantity (Current: {stock[fruit_name]['qty']}kg): ").strip()
        new_price_str = input(f"Enter new price (Current: ${stock[fruit_name]['price']}): ").strip()
        
        if new_qty_str:
            stock[fruit_name]['qty'] = int(new_qty_str)
        if new_price_str:
            stock[fruit_name]['price'] = float(new_price_str)
            
        save_data(stock)
        msg = f"Manager updated {fruit_name} stock."
        print(f"\nSuccess: {msg}")
        log_transaction(msg)
        
    except ValueError:
         print("Unexpected input! Returning to previous menu. No changes made.")