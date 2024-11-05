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

    def get_balance(self):
        return self.__balance

my_account = BankAccount("Bonaventure")

amount = float(input("Deposit amount: "))
my_account.deposit(amount)

print(my_account.get_balance())
