import record as r
import goal as g
import currencies as c
import cowsay
from colorama import init, Fore

init()

print(Fore.CYAN)
cowsay.milk('Welcome to the Budget Calculator!')
print(Fore.RESET)

saving_goal = g.set_goal()

r.add(r.Transactions.deposit, r.income_category, 'income')
r.add(r.Transactions.withdraw, r.expense_category, 'expense')

remain = g.balance()
print(Fore.CYAN)
if remain >= saving_goal:
    cowsay.milk('Congratulation, you\'ve achieved your saving goal!')
else:
    cowsay.milk(f'You still have to save ${saving_goal-remain} to achieve your goal.')
print(Fore.RESET)

while True:
    try:
        g.show_details()
        break
    except g.SelectError as err:
        print(err)
        print(Fore.RESET)

c.conversion(saving_goal)

print(Fore.CYAN)
cowsay.milk('Thanks for using the budget calculator. Bye ~')
print(Fore.RESET)