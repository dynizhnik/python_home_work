p = float(input('Enter amount of money:'))
r = int(input('Enter percent:')) / 100
n = int(input('Enter frequency:'))
t = int(input('Enter years:'))
a = p * (1 + r / n) ** (n * t)
print('Total money:', format(a, '.2f'))
