from datetime import date
details = []

income_category = ['Salary', 'Investment', 'Gifts']
expense_category = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Medical']

class Category:
    def __init__(self, category_list):
        self.category_list = category_list

    def instruction(self, section):
        return int(input(f'Enter an integer number to add an {section} in one of the above categories.\nEnter any integer other than 0 or the ones listed to customise a new category. \nEnter 0 to exit {section.capitalize()} Section. '))

    def options(self, category_list):
        for count, items in enumerate(category_list):
            print(count+1, items)

    def new_category(self, category_list):
        new = input('Creating a new category. Please enter the name of the new category: ')
        return category_list.append(new.capitalize())

    def show_balance(self):
        title = "-"*23 + "Budget Report" + "-"*23 + "\n"
        items = ""
        total = 0
        date_printed = date.today()
        for item in details:
            items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"

            total += item['amount']

        output = title + items + "\nBalance: " + str(total) + "\nDate Printed: " + str(date_printed)
        print(output)

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

def add(deposit_or_withdraw, income_or_expense, section):
    while True:
        display = Category(income_or_expense)
        display.options(income_or_expense)

        try:
            x = display.instruction(section)
    
            if x in range (1, len(income_or_expense)+1):
                category = income_or_expense[x-1]
                description = input(f'Enter the {section} description: ')
    
                while True:
                    try:
                        amount = float(input(f'Enter the {section} amount: '))
                        break
                    except ValueError:
                        print('\nPlease enter a number.\n')
    
                deposit_or_withdraw(Transactions(category, description, amount))

            elif x == 0:
                break
    
            elif x < 0 or x >= len(income_or_expense)+1:
                display.new_category(income_or_expense)
    
        except ValueError:
            print('\nPlease enter an integer.\n')