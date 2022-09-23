import cowsay
from colorama import init, Back, Style
import record as r

init()

def set_goal():
    while True:
        try:
            user_input = float(input(Style.BRIGHT + '\nDo you have a saving goal?\nEnter the amount you aim to save here: '))
            print(Back.CYAN + f'Your saving goal is: {user_input}' + Back.RESET + Style.RESET_ALL)
            break
        
        except ValueError:
            cowsay.cow('The amount entered has to be a number.')
    return user_input

def balance():
    total = 0
    for item in r.details:
        total += item['amount']
    return total
                
