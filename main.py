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
        r.show_cat_details(r.Category.income_category, 'income')
        break
    except r.RangeError as err:
        print(err)
    except ValueError:
        print('Input must be an integer.')
while True:
    try:
        r.show_cat_details(r.Category.expense_category, 'expense')
        break
    except r.RangeError as err:
        print(err)
    except ValueError:
        print(Fore.RED)
        cowsay.cow('Input must be an integer.')
        print(Fore.RESET)

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
        print(err)
    except ValueError:
        print(Fore.RED)
        cowsay.cow('Input has to be a number.')
        print(Fore.RESET)

c.exchange(user_input)

print(Fore.CYAN)
cowsay.milk('Thanks for using the budget calculator. Bye ~')
print(Fore.RESET)