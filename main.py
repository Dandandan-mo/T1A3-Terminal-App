import record as r
import goal as g
import currencies as c
import cowsay

cowsay.milk('Welcome to the Budget Calculator! ')

saving_goal = g.set_goal()

r.add(r.Transactions.deposit, r.income_category, 'income')
r.add(r.Transactions.withdraw, r.expense_category, 'expense')

remain = g.balance()
if remain >= saving_goal:
    cowsay.milk('Congratulation, you\'ve achieved your saving goal!')
else:
    cowsay.milk(f'You still have to save {saving_goal-remain} to achieve your goal.')

while True:
    try:
        g.show_details()
        break
    except g.SelectError as err:
        print(err)

if remain > 0:
    c.conversion(remain)

cowsay.milk('Thanks for using the budget calculator. Bye ~')