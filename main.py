import features as f
import cowsay

cowsay.cow('Welcome to the budget calculater!\n')

f.add(f.Transactions.deposit, f.income_category, 'income')
f.add(f.Transactions.withdraw, f.expense_category, 'expense')

f.Category(f.income_category.append(f.expense_category)).show_balance()


