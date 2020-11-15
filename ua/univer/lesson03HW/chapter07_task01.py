WEEK = 7

sale_day = []
sale_total = 0.0
for i in range(WEEK):
    sale = float(input(f'Enter {i+1} day: '))
    sale_day.append(sale)
    sale_total += sale
print('All sales by days:', sale_day)
print('Total sales:', format(sale_total,'.2f'))