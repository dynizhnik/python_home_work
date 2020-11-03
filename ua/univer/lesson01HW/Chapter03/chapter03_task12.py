PRICE = 99
SALE_10 = 10
SALE_20 = 20
SALE_30 = 30
SALE_40 = 40

count = int(input('Enter count of software that you bought: '))
if count in range(0, 10):
    total = count * PRICE
    print('You haven`t sale.')
    print('Total price is ', format(total, '.2f'), '$', sep='')
elif count in range(10, 20):
    total = (count - 9) * PRICE * (100 - SALE_10) / 100 + 9 * PRICE
    print(f'Your score is {SALE_10}')
    print('Total price is ', format(total, '.2f'), '$', sep='')
elif count in range(20, 50):
    total = (count - 19) * PRICE * (100 - SALE_20) / 100 + \
            10 * PRICE * (100 - SALE_10) / 100 + 9 * PRICE
    print(f'Your score is {SALE_20}')
    print('Total price is ', format(total, '.2f'), '$', sep='')
elif count in range(50, 100):
    total = (count - 49) * PRICE * (100 - SALE_30) / 100 + \
            30 * PRICE * (100 - SALE_20) / 100 + \
            10 * PRICE * (100 - SALE_10) / 100 + 9 * PRICE
    print(f'Your score is {SALE_30}')
    print('Total price is ', format(total, '.2f'), '$', sep='')
elif count >= 100:
    total = (count - 99) * PRICE * (100 - SALE_40) + \
            50 * PRICE * (100 - SALE_30) / 100 + \
            30 * PRICE * (100 - SALE_20) / 100 + \
            10 * PRICE * (100 - SALE_10) / 100 + 9 * PRICE
    print(f'Your score is {SALE_40}')
    print('Total price is ', format(total, '.2f'), '$', sep='')
else:
    print('Error count!')
