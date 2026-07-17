# Bank Account Class using OOP

class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= self.balance:
            self.balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Current Balance: ₹", self.balance)


account = BankAccount()

while True:

    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account.deposit()

    elif choice == "2":
        account.withdraw()

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank You for using our Bank System!")
        break

    else:
        print("Invalid Choice!")