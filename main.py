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
r.show_cat_details()

remain = g.balance()
set_goal = g.Comparison(remain)
goal = set_goal.input_goal()
set_goal.compare_goal()

c.enter()

while True:
    try:
        user_input = c.receive(goal, remain)
        break
    except c.InputError as err:
        cowsay.cow(err)

c.exchange(user_input)

print(Fore.CYAN)
cowsay.milk('Thanks for using the budget calculator. Bye ~')
print(Fore.RESET)