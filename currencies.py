from py_currency_converter import convert
from colorama import init, Fore, Back, Style
import cowsay

init()

currency_types = {'NZD': 'New Zealand Dollar', 'USD': 'United States Dollar', 'EUR': "Euro", 'CNY': 'Chinese Renminbi', 'JPY': 'Janpaniese Yen', 'GBP': 'Pound Sterling', 'CHF': 'Swiss Franc', 'CAD': 'Canandian Dollar', 'ZAR': 'South African Rand'}

option = ['saving goal', 'remaining balance', 'a new input amount']

class InputError(Exception):
    pass

def receive(choice_1, choice_2):
    print(Fore.MAGENTA)
    for count, items in enumerate(option):
        print(count+1, items)
    print(Fore.RESET)
    user_input = input('Enter a number to choose which amount you want to convert: ')
    if user_input == '1':
        user_input = choice_1
    elif user_input == '2':
        user_input = choice_2
    elif user_input == '3':
        user_input = float(input('Enter another amount: '))
    else:
        print(Fore.RED)
        raise InputError(cowsay.get_output_string('cow', 'input has to be 1, or 2, or 3'))
    return user_input

def exchange(user_input):
    for key, value in currency_types.items():
        print(Fore.MAGENTA + f'The code for {value} is {key}')
        print(Fore.RESET)
    
    while True:
        select_currency = input(Style.BRIGHT + '\nEnter a currency code to convert Australian Dollar into another currency (See examples of some code above).\nEnter 0 to exit and terminate the app. ')
        print(Style.RESET_ALL)

        if select_currency in list(currency_types.keys()):
            converted = convert(base='AUD', amount=user_input, to=[select_currency])
            for key, value in converted.items():
                print(Style.BRIGHT)
                print(Back.CYAN + f'\n{user_input} AUD is equal to {round(value, 1)} {key}' + Back.RESET)
            print(Style.RESET_ALL)

        elif select_currency == '0':
            break
        else:
            print(Fore.RED)
            cowsay.cow('Wrong code, try again.')
            print(Fore.RESET)

def enter():
    while True:
        user_enter = input(Style.BRIGHT + 'Enter "c" to continue. ')
        print(Style.RESET_ALL)
        if user_enter == 'c':
            break
        else:
            continue

    print('\nThis budget calculator supports currency convertion.\n')


    