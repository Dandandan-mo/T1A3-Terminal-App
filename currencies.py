from py_currency_converter import convert
from colorama import init, Fore, Back, Style
import cowsay

init()

currency_types = {'NZD': 'New Zealand Dollar', 'USD': 'United States Dollar', 'EUR': "Euro", 'CNY': 'Chinese Renminbi', 'JPY': 'Janpaniese Yen', 'GBP': 'Pound Sterling', 'CHF': 'Swiss Franc', 'CAD': 'Canandian Dollar', 'ZAR': 'South African Rand'}

def conversion(goal):
    print('-'*59)
    print('This budget calculator supports currency convertion.\n')

    for key, value in currency_types.items():
        print(Fore.MAGENTA + f'The code for {value} is {key}')
        print(Fore.RESET)

    while True:
        select_currency = input(Style.BRIGHT + '\nEnter a currency code to convert your saving goal in Australian Dollar into another currency.\nEnter 0 to exit and terminate the app. ')
        print(Style.RESET_ALL)

        convert_currencies = convert(base='AUD', amount=goal, to=[select_currency])

        if select_currency in list(currency_types.keys()):
            for key, value in convert_currencies.items():
                print(Style.BRIGHT)
                print(Back.CYAN + f'\n{goal} AUD is equal to {round(value, 1)} {key}' + Back.RESET)
                print(Style.RESET_ALL)

        elif select_currency == '0':
            break
        else:
            print(Fore.RED)
            cowsay.cow('Wrong code, try again.')
            print(Fore.RESET)
