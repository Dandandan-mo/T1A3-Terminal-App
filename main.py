import features as f

print('''
Welcome to the budget tracker!
This app helps you track your incomes and expenses.
''')

while True:
    display = f.Category(f.income_category)
    display.options(f.income_category)

    try:
        x = display.instruction('income')

        if x in range (1, len(f.income_category)+1):
            category = f.income_category[x-1]
            description = input('Enter description for the income: ')

            while True:
                try:
                    amount = float(input('Enter the amount: '))
                    break
                except ValueError:
                    print('\nPlease enter a number.\n')

            user_income = f.Transactions(category,description, amount)
            user_income.deposit()

        elif x == 0:
            print('You\'ve exited Income Section and entered Expense Section.')
            break

        elif x < 0 or x >= len(f.income_category)+1:
            display.new_category(f.income_category)

    except ValueError:
        print('\nPlease enter an integer.\n')

while True:
    display = f.Category(f.expense_category)
    display.options(f.expense_category)

    try:
        x = display.instruction('expense')

        if x in range (1, len(f.expense_category)+1):
            category = f.expense_category[x-1]
            description = input('Enter description for the expense: ')

            while True:
                try:
                    amount = float(input('Enter the amount: '))
                    break
                except ValueError:
                    print('\nPlease enter a number.\n')
            user_expense = f.Transactions(category, description, amount)
            user_expense.withdraw()

        elif x == 0:
            print('You\'ve exited Expense Section. Printing budget report...\n')
            break

        elif x < 0 or x >= len(f.expense_category)+1:
            display.new_category(f.expense_category)
        
    except ValueError:
        print('\nPlease enter an integer.\n')

display.show_balance()
