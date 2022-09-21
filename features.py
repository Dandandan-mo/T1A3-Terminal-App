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
        new = input('Please enter the name of the category: ')
        return category_list.append(new.capitalize())

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

class Transactions:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount
        self.details = details

    def add(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': self.amount})

    def withdraw(self):
        self.details.append({'category': self.category, 'description': self.description, 'amount': -self.amount})

