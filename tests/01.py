class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute
        self.__batata = 1
        self._cebola = 1
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, value):
        if value > 0:
            self.__balance += value
            return True
        return False
    
    def withdraw(self, value):
        if 0 < value <= self.__balance:
            self.__balance -= value
            return True
        return False

# Example usage:
account = Account(100)
account.deposit(50)
print(account.balance)  # 150
account.withdraw(30)
print(account.balance)  # 120
# print(account.__batata) 2 underlines => error
print(account._cebola) # 1 underline => ok