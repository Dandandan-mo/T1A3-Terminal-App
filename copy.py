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

income_category = ['Salary', 'Investment', 'Gifts']
expense_category = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Medical']

def instruction(section):
    return int(input(f'''Enter an integer number to add an {section} in one of the above categories. Enter any integer other than 0 or the ones listed to customise a new category. Enter 0 to exit {section.capitalize()} Section.'''))

def options(a_category):
    for count, items in enumerate(a_category):
        print(count+1, items)

def new_category(a_category_item):
    new = input('Please enter the name of the category: ')
    return a_category_item.append(new.capitalize())

class Balance:
    # def __init__(self, name):
    #     self.name = name

    def __str__(self):
        title = "_"*23 + "Budget Report" + "_"*23 + "\n"
        items = ""
        total = 0
        for item in details:
            items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"

            total += item['amount']

        output = title + items + "Balance: " + str(total)
        return output

    # def display_incomes(self, category):

class Category:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': self.amount})

    def withdraw(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': -self.amount})

# main.py"
import features as f

print('''
Welcome to the budget tracker!
This app helps you track your incomes and expenses.
''')

while True:
    display = f.Category(f.income_category)
    display.options(f.income_category)

    x = display.instruction('income')

    if x in range (1, len(f.income_category)+1):
        category = f.income_category[x-1]
        description = input('Enter description for the income: ')
        amount = float(input('Enter the amount: '))
        user_income = f.Transactions(category, description, amount)
        user_income.add()

    elif x == 0:
        print('You\'ve exited Income Section and entered Expense Section.')
        break

    elif x < 0 or x >= len(f.income_category)+1:
        display.new_category(f.income_category)

while True:
    display = f.Category(f.expense_category)
    display.options(f.expense_category)

    x = display.instruction('expense')

    if x in range (1, len(f.expense_category)+1):
        category = f.expense_category[x-1]
        description = input('Enter description for the expense: ')
        amount = float(input('Enter the amount: '))
        user_expense = f.Transactions(category, description, amount)
        user_expense.withdraw()

    elif x == 0:
        print('You\'ve exited Expense Section. Printing budget report...\n')
        break

    elif x < 0 or x >= len(f.expense_category)+1:
        display.new_category(f.expense_category)

display.show_balance()
