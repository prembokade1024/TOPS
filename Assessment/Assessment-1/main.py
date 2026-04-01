from manager import manager_menu
from customer import customer_menu
from utils import log_transaction

def main():
    """Main application controller."""
    log_transaction("Application Started.")
    print("Welcome to the Fruit Store!")
    
    while True:
        print("\n" + "="*30)
        print("          MAIN MENU          ")
        print("="*30)
        print("1. Fruit Manager")
        print("2. Customer")
        print("3. Exit Application")
        
        choice = input("Enter your role (1-3): ").strip()
        
        if choice == '1':
            manager_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            print("\nThank you for using the Fruit Store Application. Goodbye!")
            log_transaction("Application Exited Cleanly.")
            break
        else:
            print("Invalid Selection! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    # Exception handling at the root level to prevent unexpected crashes
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication forcefully terminated by user.")
        log_transaction("Application Exited Unexpectedly (KeyboardInterrupt).")
    except Exception as e:
        print(f"\n\nA critical error occurred: {e}")
        log_transaction(f"CRITICAL CRASH: {e}")