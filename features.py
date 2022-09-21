from datetime import date
details = []

income_category = ['Salary', 'Investment', 'Gifts']
expense_category = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Medical']

class Category:
    def __init__(self, category_list):
        self.category_list = category_list

    def instruction(self, section):
        return int(input(f'''Enter an integer number to add an {section} in one of the above categories. Enter any integer other than 0 or the ones listed to customise a new category. Enter 0 to exit {section.capitalize()} Section.'''))

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

        output = title + items + "\nBalance: " + str(total) + "\n\nDate Printed: " + str(date_printed) + "\n"
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

