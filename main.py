import features as f

print('''
Welcome to the budget tracker!
This app helps you track your incomes and expenses.
''')

f.add(f.Transactions.deposit, f.income_category, 'income')
f.add(f.Transactions.withdraw, f.expense_category, 'expense')

f.Category(f.income_category.append(f.expense_category)).show_balance()
