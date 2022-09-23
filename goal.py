import cowsay
from colorama import init, Fore, Back, Style
import record as r

init()

def balance():
    total = 0
    for item in r.details:
        total += item['amount']
    return total

class Comparison:
    def __init__(self, remain):
        self.remain = remain
        self.goal = 0

    def input_goal(self):
        while True:
            try:
                self.goal = float(input(Style.BRIGHT + '\nDo you have a saving goal?\nEnter the amount you aim to save here: '))
                print(Back.CYAN + f'Your saving goal is: {self.goal}' + Back.RESET + Style.RESET_ALL)
                break
        
            except ValueError:
                print(Style.RESET_ALL)
                print(Fore.RED)
                cowsay.cow('The amount entered has to be a number.')
                print(Fore.RESET)
        return self.goal
            
    def compare_goal(self):
        print(Fore.CYAN)
        if self.remain >= self.goal:
            outcome = cowsay.milk('Congratulation, you\'ve achieved your saving goal!')
        else:
            outcome = cowsay.milk(f'You still have to save ${self.goal-self.remain} to achieve your goal.')
        print(Fore.RESET)
        return outcome