# 5. Упрощённая банковская система
# Создай класс BankAccount:
# Статический атрибут bank_name = "PythonBank"
# Статический атрибут accounts = {} (словарь всех счетов по номеру)
# Статический метод get_account(account_number) — должен возвращать
# объект счёта по номеру или None, если счёта нет
# Сам объект BankAccount должен содержать:
# атрибуты: number, owner, balance
# метод deposit(amount)
# метод withdraw(amount)
# При создании каждого счёта он должен
# автоматически регистрироваться в BankAccount.accounts.
import random


class BankAccount:
    __bank_name = "PythonBank"
    __accounts = {}

    # @classmethod
    # @property
    # def bank_name(cls):
    #     return cls.__bank_name

    # @bank_name.setter
    # def bank_name(cls, name):
    #     cls.__bank_name = name

    # @classmethod
    # @property
    # def get_accounts(cls):
    #     if input("введите пароль") == "1234":
    #         return cls.__accounts
    #     else:
    #         return None

    @classmethod
    def get_account(cls, account_number):
        if account_number in cls.__accounts.keys():
            return cls.__accounts[account_number]
        else:
            return None

    @classmethod
    def get_random_number(cls):
        numbers = random.randint(100000, 999999)
        if cls.get_account(numbers):
            numbers = cls.get_random_number()
        return numbers

    def __init__(self, owner, balance):
        self.number = BankAccount.get_random_number()
        self.owner = owner
        self.balance = balance
        BankAccount.__accounts[self.number] = self

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return f"BankAccount {self.number} with balance {self.balance}"


acc = BankAccount("Человек", 100)
print(acc)

# print(BankAccount.get_accounts)