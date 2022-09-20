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
        category = income_category[x-1]
        description = input('Enter description for the income: ')
        amount = float(input('Enter the amount: '))
        user_income = features.Category(category, description, amount)
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
        category = expense_category[x-1]
        description = input('Enter description for the expense: ')
        amount = float(input('Enter the amount: '))
        user_expense = features.Category(category, description, amount)
        user_expense.withdraw()
        # user_expense.display()
    elif x == 0:
        print('Printing budget report...\n')
        break

print(features.TotalBalance())
