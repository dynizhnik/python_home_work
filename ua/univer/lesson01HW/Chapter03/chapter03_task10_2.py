COIN1 = 5
COIN2 = 10
COIN3 = 50
number1 = int(input(f'Enter number of {COIN1} coins:'))
number2 = int(input(f'Enter number of {COIN2} coins:'))
number3 = int(input(f'Enter number of {COIN3} coins:'))

total = number1 * COIN1 + number2 * COIN2 + number3 * COIN3
if total == 100:
    print('Congratulation you winner, total = 1$.')
elif total < 100:
    print('Sorry, total < 1$.')
else:
    print('Sorry, total > 1$.')