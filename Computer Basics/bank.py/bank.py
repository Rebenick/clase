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
