price1 = float(input('Input price 1:'))
price2 = float(input('Input price 2:'))
price3 = float(input('Input price 3:'))
price4 = float(input('Input price 4:'))
price5 = float(input('Input price 5:'))
total_tax = (price1 + price2 + price3 + price4 + price5) * 0.07
total_price = price1 + price2 + price3 + price4 + price5 + total_tax
print('Your tax is:', for10mat(total_tax, '.2f'), 'and total price is:', format(total_price, '.2f'))