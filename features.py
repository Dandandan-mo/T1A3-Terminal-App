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

