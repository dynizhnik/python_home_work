price = float(input('Enter price: '))
tip = price * 0.18
tax = price * 0.07
total_price = price + tip + tax
print('Tip:', format(tip, '18.2f'))
print('Tax:', format(tax, '18.2f'))
print('Total price:', format(total_price, '10.2f'))