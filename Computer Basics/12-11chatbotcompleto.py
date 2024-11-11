class BankAccount:
    def __init__(self, account_number): #dinero inicial
        self.account_number = account_number
        self.money = 0

    def get_money(self): #Dinero en la cuenta
        return self.money

    def __str__(self): #Mas datos de la cuenta
        return f"Account {self.account_number}" 
    
    def deposit(self, amount): #Depositar dinero
        self.money += amount
        print(f"Has been deposited ${amount}. Actual money: ${self.money}")

    def withdraw(self, amount): #sacar dinero
        if amount <= self.money:
            self.money -= amount
            print(f"Has been withdrawn ${amount}. Actual money: ${self.money}")
        else:
            print("Not enough funds to withdraw this amount")

#Ejemplo 
cuenta = BankAccount("8932901")
cuenta.deposit(3000)
cuenta.withdraw(1502)
print(f"Final account money: ${cuenta.get_money()}")
print(cuenta)




class SavingsAccount (BankAccount):
    def __init__(self, account_number, interest_rate=0.01):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def add_interest(self, months):
        interest = self.money * self.interest_rate * (months / 12)
        self.deposit(interest)
        print(f"Added interest for {months} months.")




class CheckingAccount(BankAccount):
    def __init__(self, account_number, overdraft_limit=500):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.money + self.overdraft_limit:
            self.money -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.money}")
        else:
            print("Exceeded overdraft limit")


def chatbot():
    # Mensaje para que el usuario elija el tipo de cuenta
    print("Choose account type:")
    print("1. Savings Account")  # Opción para cuenta de ahorros
    print("2. Checking Account")  # Opción para cuenta corriente
    print("3. BankAccount")  # Opción para cuenta corriente
    account_type = input("Select an option:")  # El usuario elige la opción


    # Crear la cuenta según el tipo seleccionado
    if account_type == '1':  # Si elige una cuenta de ahorros
        account = SavingsAccount("12345", interest_rate=0.02)  # interés del 2%


    elif account_type == '2':  # Si elige una cuenta corriente
        account = CheckingAccount("12345", overdraft_limit=300)  # límite de 300

        
    elif account_type == '3':  # cuenta normal
        account = BankAccount("12345")  


    else:  # Si elige una opción no válida
        print("Invalid option, exiting.")  # Mostramos un mensaje de error
        return  # Salimos



    while True:
        print("\nWelcome to the bank account chatbot") 
        print("1. Check money")  # Opción para ver el saldo
        print("2. Deposit money")  # Opción para depositar dinero
        print("3. Withdraw money")  # Opción para retirar dinero


        if isinstance(account, SavingsAccount):  # Si es una cuenta de ahorros mostramos la opción de intereses
            print("4. Add interest")  

        print("5. Exit")  # Opción para salir

        choice = input("Select an option:")  



        if choice == '1':  # Si elige ver el saldo
            print(f"Current money: ${account.get_money()}")  # Muestra el saldo actual


        elif choice == '2':  # Si elige depositar dinero
            amount = float(input("Enter the amount to deposit: "))  # Pide la cantidad a depositar
            account.deposit(amount)  


        elif choice == '3':  # Si elige retirar dinero
            amount = float(input("Enter the amount to withdraw: "))  # Pide la cantidad a retirar
            account.withdraw(amount)  


        elif choice == '4' and isinstance(account, SavingsAccount):  # Si es cuenta de ahorros y elige agregar interés
            months = int(input("Enter the number of months for interest: "))  # Pide el número de meses
            account.add_interest(months) 


        elif choice == '5':  # Si elige salir
            print("Exiting the chatbot.")  
            break  



        else:  # Si elige una opción no válida
            print("Invalid option, please try again.")  # Mensaje de error

chatbot()  
