import features as f

f.cowsay.cow('Welcome to the budget calculater!\n')

while True:
    try:
        saving_goal = float(input('This app help calculate your incomes and expenses to see if you meet your saving goal. \nEnter the amount you aim to save here: '))
        print(f'Your saving goal is: {saving_goal}')
        break
        
    except ValueError:
        f.cowsay.cow('The amount entered has to be a number.')

f.add(f.Transactions.deposit, f.income_category, 'income')
f.add(f.Transactions.withdraw, f.expense_category, 'expense')

remain = f.balance()
if remain >= saving_goal:
    f.cowsay.milk('Congratulation, you\'ve achieved your saving goal!')
else:
    f.cowsay.cheese(f'You still have to save {saving_goal-remain} to achieve your goal.')

while True:
    try:
        f.show_details()
        break
    except f.SelectError as err:
        print(err)