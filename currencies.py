from py_currency_converter import convert
import cowsay
import goal as g

currency_types = {'NZD': 'New Zealand Dollar', 'USD': 'United States Dollar', 'EUR': "Euro", 'CNY': 'Chinese Renminbi', 'JPY': 'Janpaniese Yen', 'GBP': 'Pound Sterling', 'CHF': 'Swiss Franc', 'CAD': 'Canandian Dollar', 'ZAR': 'South African Rand'}

# remain_balance = 100

# format the input and output
# decimal points

def conversion(remain_balance):
    print('This budget calculator supports currency convertion.\nBelow is a list of codes for supported currencies:\n')

    for key, value in currency_types.items():
        print(f'The code for {value} is {key}')

    while True:
        select_currency = input('\nEnter a code to convert your remaining balance in Australian Dollar into another currency.\nEnter 0 to exit and terminate the app. ')

        convert_currencies = convert(base='AUD', amount=remain_balance, to=[select_currency])

        if select_currency in list(currency_types.keys()):
            for key, value in convert_currencies.items():
                print(f'{remain_balance} AUD is equal to {round(value, 1)} {key}')
        elif select_currency == '0':
            break
        else:
            cowsay.cow('Wrong code, try again.')
