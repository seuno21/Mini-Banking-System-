# Mini Banking System Project
# By: Oluwaseun okuneye

def display_menu():
    print("\n--- Welcome to the Python Bank ---")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Customers")
    print("6. Exit")


def create_account(accounts):
    try:
        name = input("Enter customer name: ").strip().title()  
        if name in accounts:
            print("Account already exists!")
            return
        
        initial_balance = float(input("Enter initial deposit: "))
        accounts[name] = initial_balance
        print(f"Account created successfully for {name} with balance ${initial_balance:.2f}")
    except ValueError:
        print("Invalid amount entered. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


def deposit(accounts):
    try:
        name = input("Enter your name: ").strip().title()
        if name in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[name] += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${accounts[name]:.2f}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid amount entered. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


def withdraw(accounts):
    try:
        name = input("Enter your name: ").strip().title()
        if name in accounts:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= accounts[name]:
                accounts[name] -= amount
                print(f"Successfully withdrew ${amount:.2f}. New balance: ${accounts[name]:.2f}")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid amount entered. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_balance(accounts):
    try:
        name = input("Enter your name: ").strip().title()
        if name in accounts:
            print(f"Account Balance for {name}: ${accounts[name]:.2f}")
        else:
            print("Account not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_customers(accounts):
    if not accounts:
        print("No customers in the system.")
        return
    print("\n--- Customer List ---")
    for name, balance in accounts.items():
        print(f"{name}: ${balance:.2f}")


def run_banking_system():
    accounts = {}  # Store account details
    while True:
        display_menu()
        try:
            choice = int(input("Select an option (1-6): "))
            if choice == 1:
                create_account(accounts)
            elif choice == 2:
                deposit(accounts)
            elif choice == 3:
                withdraw(accounts)
            elif choice == 4:
                check_balance(accounts)
            elif choice == 5:
                view_customers(accounts)
            elif choice == 6:
                print("Thank you for using Python Bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")

        cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if cont not in {'yes', 'y'}:
            print("Exiting system. See you next time!")
            break


# Run program
run_banking_system()
