class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name: *^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'] [0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"

            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, "description": description})

    def withdraw(self, amount, description=""):
        self.ledger.append({'amount': -amount, 'description': description})

    def git_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item['amount']

        return total_cash

# features.py:
details = []
class TotalBalance:
    # def __init__(self, name):
    #     self.name = name

    def __str__(self):
        title = "_"*26 + "Summary" + "_"*26 + "\n"
        items = ""
        total = 0
        for item in details:
            items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"

            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

class Income:
    def __init__(self, c_category, c_description, c_amount):
        self.category = c_category
        self.description = c_description
        self.amount = c_amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': self.amount})

    # def display(self):
    #     print(self.details)


class Expense:
    def __init__(self, d_category, d_description, d_amount):
        self.category = d_category
        self.description = d_description
        self.amount = d_amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': -self.amount})

    # def display(self):
    #     print(self.details)

# main.py"
import features

print('''
Welcome to the budget tracker!
This app helps you track your incomes and expenses.
''')

income_category = ['Salary', 'Investment', 'Gifts']
expense_category = ['Housing', 'Food', 'Transportation', 'Utilities', 'Medical']

while True:
    for count, items in enumerate(income_category):
        print(count+1, items)

    x = int(input('''Enter a number to add an income in one of the above categories. Enter 0 to exit income change to the Expense section.'''))
    
    if x in range (1, 4):
        c_category = income_category[x-1]
        c_description = input('Enter description for the income: ')
        c_amount = float(input('Enter the amount: '))
        user_income = features.Income(c_category, c_description, c_amount)
        user_income.add()
        # user_income.display()
    elif x == 0:
        print('Now choose a category for the expense.')
        break

while True:
    for count, items in enumerate(expense_category):
        print(count+1, items)

    x = int(input('''Enter a number to add an expense in one of the above categories. Enter 0 to exit and print budget report.'''))
    if x in range (1, 6):
        d_category = expense_category[x-1]
        d_description = input('Enter description for the expense: ')
        d_amount = float(input('Enter the amount: '))
        user_expense = features.Expense(d_category, d_description, d_amount)
        user_expense.add()
        # user_expense.display()
    elif x == 0:
        print('Printing budget report...\n')
        break

print(features.TotalBalance())
