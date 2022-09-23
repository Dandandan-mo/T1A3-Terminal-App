import record as r
import goal as g
import currencies as c
import cowsay
from colorama import init, Fore

init()

print(Fore.CYAN)
cowsay.milk('Welcome to the Budget Calculator!')
print(Fore.RESET)

r.add(r.Transactions.deposit, r.Category.income_category, 'income')
r.add(r.Transactions.withdraw, r.Category.expense_category, 'expense')

r.show_details()

while True:
    try:
        r.show_subtotal(r.Category.income_category, 'income')
        break
    except r.SelectError as err:
        print(err)

while True:
    try:
        r.show_subtotal(r.Category.expense_category, 'expense')
        break
    except r.SelectError as err:
        print(err)

saving_goal = g.set_goal()
remain = g.balance()
print(Fore.CYAN)
if remain >= saving_goal:
    cowsay.milk('Congratulation, you\'ve achieved your saving goal!')
else:
    cowsay.milk(f'You still have to save ${saving_goal-remain} to achieve your goal.')
print(Fore.RESET)

c.conversion(saving_goal)

print(Fore.CYAN)
cowsay.milk('Thanks for using the budget calculator. Bye ~')
print(Fore.RESET)