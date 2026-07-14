def get_amount():
    while True:
        try:
            amount = float(input('Enter amount to convert: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid Amount!')

def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD', 'AUD', 'PHP', 'JPY', 'KRW')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD/AUD/PHP/JPY/KRW): ').upper()
        if currency not in currencies:
            print('Invalid Currency!')
        else:
            return currency

def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR': 0.88, 'CAD': 1.41, 'AUD': 1.44, 'PHP': 61.58, 'JPY': 162.15, 'KRW': 1495.05},
        'EUR': {'USD': 1.14, 'CAD': 1.61, 'AUD': 1.65, 'PHP': 70.32, 'JPY': 185.36, 'KRW': 1708.05},
        'CAD': {'USD': 0.71, 'EUR': 0.62, 'AUD': 1.02, 'PHP': 43.55, 'JPY': 114.72, 'KRW': 1057.97},
        'AUD': {'USD': 0.69, 'EUR': 0.61, 'CAD': 0.98, 'PHP': 42.74, 'JPY': 112.57, 'KRW': 1037.77},
        'PHP': {'USD': 0.016, 'EUR': 0.014, 'CAD': 0.023, 'AUD': 0.023, 'JPY': 2.62, 'KRW': 24.28},
        'JPY': {'USD': 0.0062, 'EUR': 0.0054, 'CAD': 0.0087, 'AUD': 0.0089, 'PHP': 0.38, 'KRW': 9.22},
        'KRW':{'USD': 0.00067, 'EUR': 0.00059, 'CAD': 0.00095, 'AUD': 0.00096, 'PHP': 0.041, 'JPY': 0.11}
    }

    if source_currency == target_currency:
        return amount

    return amount * exchange_rates[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')

if __name__ == '__main__':
    main()