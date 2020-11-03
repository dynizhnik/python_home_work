PRICE_1 = 150
PRICE_2 = 300
PRICE_3 = 400
PRICE_4 = 475

weight = int(input("Enter weight your post package: "))
if weight in range (1,201):
    total_price = weight * PRICE_1 / 100
    print('Total price is ', format(total_price, '.2f'), '$', sep='')
elif weight in range (201,601):
    total_price = weight * PRICE_2 / 100
    print('Total price is ', format(total_price, '.2f'), '$', sep='')
elif weight in range(601, 1000):
    total_price = weight * PRICE_3 / 100
    print('Total price is ', format(total_price, '.2f'), '$', sep='')
elif weight >= 1000:
    total_price = weight * PRICE_4 / 100
    print('Total price is ', format(total_price, '.2f'), '$', sep='')
else:
    print('Error weight!')