import cowsay
from colorama import init, Fore, Style
init()

details = []

income_category = ['Salary', 'Investment', 'Gifts']
expense_category = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Medical']

class Category:
    def __init__(self, category_list):
        self.category_list = category_list

    def options(self):
        for count, items in enumerate(self.category_list):
            print(count+1, items)

    def new_category(self):
        new = input(Style.BRIGHT + '\nCreating a new category. Please enter the name of the new category: ')
        print(Style.RESET_ALL)
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
    return int(input(Style.BRIGHT + f'Enter an integer number to add an {section} in one of the above categories.\nEnter any integer other than 0 or the ones listed to customise a new category. \nEnter 0 to move on when finish adding all {section} transactions. ' + Style.RESET_ALL))

def add(deposit_or_withdraw, income_or_expense, section):
    while True:
        print('-'*59)
        print(Fore.MAGENTA + f'{section.upper()}\n')
        display = Category(income_or_expense)
        display.options()
        print(Fore.RESET)

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
                        print(Fore.RED)
                        cowsay.cow('Please enter a number.')
                        print(Fore.RESET)
    
                deposit_or_withdraw(Transactions(category, description, amount))

            elif x == 0:
                break
    
            elif x < 0 or x >= len(income_or_expense)+1:
                display.new_category()
    
        except ValueError:
            print(Fore.RED)
            cowsay.cow('Please enter an integer. ')
            print(Fore.RESET)



