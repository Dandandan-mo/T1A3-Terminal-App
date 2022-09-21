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
        print('You\'ve exited Income Section.')
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
        print('Printing budget report...\n')
        break

    elif x < 0 or x >= len(f.expense_category)+1:
        display.new_category(f.expense_category)

print(f.Balance())
