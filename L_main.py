from L_features import Category

home = Category('Home')
food = Category('Food')
transportation = Category('Transportation')
medical = Category('Medical')
entertainment = Category('Entertainment')

print('''
Welcome to the budget tracker!
This app helps you track your incomes and expenses.
''')

expense_category = ['Home', 'Food', 'Transportation', 'Medical', 'Entertainment']

while True:
    for count, items in enumerate(expense_category):
        print(count+1, items)

    x = int(input('''Enter a number to add an expense in one of the above categories. Enter 0 to exit income change to the Expense section.'''))
    if x == 0:
        break
    elif x in range (1, 6):
        user_expense = Category(expense_category[x-1])
        description = input('Enter the description for the expense: ')
        amount = float(input('Enter the amount: '))
        user_expense.withdraw(amount, description)
        print(user_expense.get_balance())

p = input('Press "p" to print the ledger: ')
if p == 'p':
    print(home)
    print(food)


