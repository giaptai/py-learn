# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display_info(self):
#         return f"Book: {self.title} by {self.author}"

# my_book = Book("1984", "George Gwell")
# my_book2 = Book("The Code Book", "Simon Singh")

# print(my_book.display_info())
# print(my_book.display_info())


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid number")
        elif amount > self.balance:
            print("Balance is not enough")
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.balance}"

    def get_balance(self):
        return f"Your current balance is {self.balance}"


bank_account = BankAccount("123", "Minh Thu", 3333)
bank_account2 = BankAccount("145", "Long Tran")

print(bank_account.deposit(100))
print(bank_account.withdraw(200))
print(bank_account.get_balance())

print(bank_account2.get_balance())
print(bank_account2.deposit(500))


