from utils import load_data, save_data, log_transaction
from manager import view_fruits

def customer_menu():
    """Displays the Customer menu and handles purchasing logic."""
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Fruits")
        print("2. Buy Fruits")
        print("3. Return to Main Menu")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            view_fruits()
        elif choice == '2':
            buy_fruit()
        elif choice == '3':
            break
        else:
            print("Invalid input! Please enter a number between 1 and 3.")

def buy_fruit():
    """Business Logic: Handle customer transaction and dictionary deduction."""
    stock = load_data()
    if not stock:
        print("\nSorry, the store is currently empty!")
        return
        
    view_fruits()
    fruit_name = input("\nEnter the name of the fruit you want to buy: ").strip().title()
    
    if fruit_name not in stock:
        print(f"Sorry, we do not have {fruit_name} in stock.")
        return
        
    try:
        qty_needed = int(input(f"How many kg of {fruit_name} do you want? "))
        
        if qty_needed <= 0:
            print("Please enter a valid amount greater than 0.")
            return
            
        if qty_needed > stock[fruit_name]['qty']:
            print(f"Insufficient stock! We only have {stock[fruit_name]['qty']}kg available.")
            return
            
        # Process transaction
        total_cost = qty_needed * stock[fruit_name]['price']
        stock[fruit_name]['qty'] -= qty_needed
        
        save_data(stock)
        msg = f"Customer bought {qty_needed}kg of {fruit_name} for ${total_cost:.2f}."
        print(f"\nSuccess: You bought {qty_needed}kg of {fruit_name}. Total Cost: ${total_cost:.2f}")
        log_transaction(msg)
        
    except ValueError:
        print("Unexpected input! Transaction cancelled. Returning to menu.")