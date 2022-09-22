import record as r
import goal as g
import cowsay

cowsay.cow('Welcome to the budget calculater!\n')

# g.set_goal()

r.add(r.Transactions.deposit, r.income_category, 'income')
r.add(r.Transactions.withdraw, r.expense_category, 'expense')

g.compare()

while True:
    try:
        g.show_details()
        break
    except g.SelectError as err:
        print(err)