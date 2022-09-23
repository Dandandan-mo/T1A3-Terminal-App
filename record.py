import cowsay
from colorama import init, Fore, Style
from datetime import date
init()

details = []

class SelectError(Exception):
    pass

class Category:

    income_category = ['Salary', 'Investment', 'Gifts']
    expense_category = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Medical']
    combined_category = income_category + expense_category

    def __init__(self, category_list):
        self.category_list = category_list

    def options(self):
        for count, items in enumerate(self.category_list):
            print(count+1, items)

    def new_category(self):
        new = input(Style.BRIGHT + '\nCreating a new category. Please enter the name of the new category: ')
        print(Style.RESET_ALL)
        return self.category_list.append(new.capitalize())

    def cat_details(self, category):
        sub = 0
        items = ''
        title = f'{category.capitalize():-^30}\n'
        for item in details:
            if category.capitalize() == item['category']:
                items += f"{item['description'][0:20]:20}" + f"{item['amount']:>9.2f}" + "\n"
                sub += item['amount']
        output = title + items + '\nSubtotal: ' + str(sub) + '\n'
        print(Fore.CYAN + output)
        print(Fore.RESET)
        
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
        print(Fore.MAGENTA + f'{section.upper()}' + 'S\n')
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

def show_details():
    print(Style.BRIGHT + 'See below your transaction details:')
    print(Style.RESET_ALL)

    title = "-"*20 + "Transaction Summary" + "-"*20 + "\n"
    items = ""
    total = 0
    date_printed = date.today()
    for item in details:
        items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"
        total += item['amount']

    output = title + items + '\nBalance: ' + str(total) + '\nDate: ' + str(date_printed) + '\n'
    print(Fore.CYAN + output)
    print(Fore.RESET)

def show_subtotal(category_list, section):
    while True:
        print(Fore.MAGENTA)
        print(f'{section.upper()}S\n')
        cat_list = Category(category_list)
        cat_list.options()
        print(Fore.RESET)
        select = input(Style.BRIGHT + 'Enter name of the category to view subtotal. Enter 0 to continue: ')
        print(Style.RESET_ALL)
        if select.capitalize() in category_list:
            cat_list.cat_details(select)
        elif select == '0':
            break
        else:
            print(Fore.RED)
            raise SelectError(cowsay.get_output_string('cow', (f'{select} is not a valid category.')))

def show_cat_details():
    while True:
        try:
            show_subtotal(Category.income_category, 'income')
            break
        except SelectError as err:
            print(err)

    while True:
        try:
            show_subtotal(Category.expense_category, 'expense')
            break
        except SelectError as err:
            print(err)