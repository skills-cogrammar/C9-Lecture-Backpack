class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited, New balance: {self.__balance}")
        else:
            print("Deposit amount must be more than 0")

    def withdraw(self, amount):
        if 0 < amount <=self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, Available Balance: {self.__balance}")
        else:
            print(f"Insufficient funds. Balance is {self.__balance}")

    def get_balance(self):
        return f"Account Balance: {self.__balance}"

my_account = BankAccount("Bonaventure")

amount = float(input("Deposit amount: "))
my_account.deposit(amount)

withdraw_amount = float(input("How much do you want to withdraw? "))
my_account.withdraw(withdraw_amount)

print(my_account.get_balance())
