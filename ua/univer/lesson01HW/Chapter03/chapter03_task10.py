COIN1 = 5
COIN2 = 10
COIN3 = 50
total = 0

if total < 100:
    coins = int(input('Enter count of coin: '))
    total +=coins
    if total < 100:
        coins = int(input('Enter count of coin: '))
        total += coins
        if total < 100:
            coins = int(input('Enter count of coin: '))
            total += coins
            if total < 100:
                coins = int(input('Enter count of coin: '))
                total += coins
                if total < 100:
                    coins = int(input('Enter count of coin: '))
                    total += coins
                    if total < 100:
                        coins = int(input('Enter count of coin: '))
                        total += coins
                    else:
                        if total == 100:
                            print('Congratulations, you are winner 1$!!!')
                        else:
                            print(format(total/100,'.2f'), 'more than 1$')
                else:
                    if total == 100:
                        print('Congratulations, you are winner 1$!!!')
                    else:
                        print(format(total/100,'.2f'), 'more than 1$')
            else:
                if total == 100:
                    print('Congratulations, you are winner 1$!!!')
                else:
                    print(format(total/100,'.2f'), 'more than 1$')
        else:
            if total == 100:
                print('Congratulations, you are winner 1$!!!')
            else:
                print(format(total/100,'.2f'), 'more than 1$')
    else:
        if total == 100:
            print('Congratulations, you are winner 1$!!!')
        else:
            print(format(total/100,'.2f'), 'more than 1$')