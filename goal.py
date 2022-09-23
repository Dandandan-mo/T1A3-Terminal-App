import cowsay
from colorama import init, Fore, Back, Style
from datetime import date
import record as r

init()

class SelectError(Exception):
    pass

def set_goal():
    while True:
        try:
            user_input = float(input(Style.BRIGHT + 'This app help track and calculate your incomes and expenses to see if you meet your saving goal.\nEnter the amount you aim to save here: '))
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
                
def show_details():
    select = input(Style.BRIGHT + 'Do you want to view your income and expense details? Y/N ')
    print(Style.RESET_ALL)

    if select == 'Y':
        title = "-"*23 + "Budget Report" + "-"*23 + "\n"
        items = ""
        total = 0
        date_printed = date.today()
        for item in r.details:
            items += f"{item['category'][0:20]:20}" + f"{item['description']:30}" + f"{item['amount']:>9.2f}" + "\n"
            total += item['amount']

        output = title + items + "\nBalance: " + str(total) + "\nDate Printed: " + str(date_printed) + "\n"
        print(Fore.CYAN + output)
        print(Fore.RESET)
    elif select == 'N':
        pass
    elif not select in ['Y', 'N']:
        print(Fore.RED)
        raise SelectError(cowsay.get_output_string('cow', (f'{select} is not a valid response. Enter "Y" or "N".')))
