from bank import BankAccount

def chatbot():
    account = BankAccount("12345")
    while True:
        print("\nWelcome to the bank account chatbot")
        print("1. Check money")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Select an option:")

        if choice == '1':
           print(f"Actualy money: ${account.get_money()}")

        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(account.deposit(amount))

        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(account.withdraw(amount))

        elif choice == '4':
            print("Exiting the chatbot.")
            break

        else:
            print("Option not valid, please try again.")

#ejecutar el chatbot
chatbot()



