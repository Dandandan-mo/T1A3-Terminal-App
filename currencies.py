from py_currency_converter import convert
# from colorama import init, Fore, Style
import cowsay

# init()

currency_types = {'NZD': 'New Zealand Dollar', 'USD': 'United States Dollar', 'EUR': "Euro", 'CNY': 'Chinese Renminbi', 'JPY': 'Janpaniese Yen', 'GBP': 'Pound Sterling', 'CHF': 'Swiss Franc', 'CAD': 'Canandian Dollar', 'ZAR': 'South African Rand'}

def conversion(goal):
    print('-'*59)
    print('This budget calculator supports currency convertion.\nBelow is a list of codes for supported currencies:\n')

    for key, value in currency_types.items():
        print(f'The code for {value} is {key}')

    while True:
        select_currency = input('\nEnter a code to convert your saving goal in Australian Dollar into another currency.\nEnter 0 to exit and terminate the app. ')

        convert_currencies = convert(base='AUD', amount=goal, to=[select_currency])

        if select_currency in list(currency_types.keys()):
            for key, value in convert_currencies.items():
                print(f'\n{goal} AUD is equal to {round(value, 1)} {key}')
        elif select_currency == '0':
            break
        else:
            cowsay.cow('Wrong code, try again.')
