from ua.univer.lesson02.Bank.account import calculate_income

while True:
    print('1. Deposit')
    print('2. Credit')
    print('3. Currency exchange')
    answer = int(input('Choice task: '))
    if answer==1:
        rate = int(input("Введите процентную ставку: "))
        money = int(input("Введите сумму: "))
        period = int(input("Введите период ведения счета в месяцах: "))
        result = calculate_income(rate, money, period)
        print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n",
      "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)
    elif answer == 0:
            break
    else:
            print('Error choice')
