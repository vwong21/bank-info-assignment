import re


class BankAccount:
    def __init__(self, name, balance):
        only_alphabet_regex = re.compile(r'([a-zA-Z]|-|_| )+')
        name_regex = re.compile(r'^[A-Z]([a-z]|-|_)+ ?(([a-z]|-|_)+ )[A-Z]([a-z]|-|_)+')
        if name == "":
            raise ValueError('Name cannot be empty')
        elif not re.match(only_alphabet_regex, name):
            raise ValueError('Name cannot include numbers or symbols')
        else:
            if re.match(name_regex, name):
                self.name = name
            else:
                raise ValueError('Invalid Name Format')

        balance = float(balance)
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        if balance >= 0:
            self.balance = balance

    def displayDetails(self):
        print(self.name)
        print(self.balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount cannot be zero or less')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount cannot be zero or less than zero')
        elif amount > self.balance:
            raise ValueError('Insufficient funds')
        elif (amount > 0) and (amount < self.balance):
            self.balance -= amount

