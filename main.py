import features as f

f.cowsay.cow('Welcome to the budget calculater!\n')

f.add(f.Transactions.deposit, f.income_category, 'income')
f.add(f.Transactions.withdraw, f.expense_category, 'expense')

f.cowsay.cow('Calculation done. This is your budget report')

f.show_balance()

f.balance('Food')


