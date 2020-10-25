buy_shares = int(input('Enter count of buy shares:'))
buy_cost = float(input('Enter purchase amount:'))
buy_tax = buy_cost * 0.03
buy_total = buy_cost + buy_tax
sale_shares = int(input('Enter count of sale shares:'))
sale_cost = float(input('Enter the sale amount:'))
sale_tax = sale_cost * 0.03
sale_total = sale_cost - sale_tax
tax_total = buy_tax + sale_tax
sum_total = sale_total - buy_total
print ('Total buy shares:      ', format(buy_total,'.2f'))
print ('Total buy tax shares:  ', format(buy_tax,'.2f'))
print ('Total sale shares:     ', format(sale_total,'.2f'))
print ('Total sale tax shares: ', format(sale_tax,'.2f'))
print ('Total sum shares:      ', format(sum_total,'.2f'))
if sum_total > 0:
    print('Joe have benefit')
else:
    print('Joe loser')