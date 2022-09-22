from datetime import date
import cowsay
from py_currency_converter import convert
import colorama

details = []

income_category = ['Salary', 'Investment', 'Gifts']
expense_category = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Medical']

class SelectError(Exception):
    pass

class Category:
    def __init__(self, category_list):
        self.category_list = category_list

    def options(self):
        for count, items in enumerate(self.category_list):
            print(count+1, items)

    def new_category(self):
        new = input('Creating a new category. Please enter the name of the new category: ')
        return self.category_list.append(new.capitalize())

class Transactions:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount
        self.details = details

    def deposit(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': self.amount})

    def withdraw(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': -self.amount})   

def instruction(section):
    return int(input(f'\nEnter an integer number to add an {section} in one of the above categories.\nEnter any integer other than 0 or the ones listed to customise a new category. \nEnter 0 when finish adding all {section} transactions. '))

def add(deposit_or_withdraw, income_or_expense, section):
    while True:
        print('-'*59)
        print(f'{section.upper()}\n')
        display = Category(income_or_expense)
        display.options()

        try:
            x = instruction(section)
    
            if x in range (1, len(income_or_expense)+1):
                category = income_or_expense[x-1]
                description = input(f'Enter the {section} description: ')
    
                while True:
                    try:
                        amount = float(input(f'Enter the {section} amount: '))
                        break
                    except ValueError:
                        cowsay.cow('Please enter a number.')
    
                deposit_or_withdraw(Transactions(category, description, amount))

            elif x == 0:
                break
    
            elif x < 0 or x >= len(income_or_expense)+1:
                display.new_category()
    
        except ValueError:
            cowsay.cow('Please enter an integer.')

def balance():
    total = 0
    for item in details:
        total += item['amount']
    return total

def show_details():
    select = input('Do you want to view your income and expense details? Y/N ')

    if select == 'Y':
        title = "-"*23 + "Budget Report" + "-"*23 + "\n"
        items = ""
        total = 0
        date_printed = date.today()
        for item in details:
            items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"
            total += item['amount']

        output = title + items + "\nBalance: " + str(total) + "\nDate Printed: " + str(date_printed) + "\n"
        print(output)
    elif select == 'N':
        pass
    elif not select in ['Y', 'N']:
        raise SelectError(cowsay.get_output_string('cow', (f'{select} is not a valid response. Enter "Y" or "N".')))




