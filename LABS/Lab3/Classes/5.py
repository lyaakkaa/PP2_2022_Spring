

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,number):
        self.balance += number
        return f'Your balance: {self.balance}'

    def Withdraw(self,number):
        if self.balance<number:
            return f'You do not have enough funds on your balance.'
        else:
            self.balance -= number
            return f'Your balance: {self.balance}'

person1 = Account('Leila',3000)
print(person1.deposit(2000))
print(person1.Withdraw(1000))