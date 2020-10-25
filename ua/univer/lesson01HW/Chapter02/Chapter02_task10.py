cookie = int(input('Enter count of cookies: '))
sugar_glass = 1.5 * cookie / 48
butter_glass = cookie / 48
flour_glass = 2.75 * cookie / 48
print('You need glasses of sugar:', format(sugar_glass, '7.2f'))
print('You need glasses of butter:', format(butter_glass, '6.2f'))
print('You need glasses of flour:', format(flour_glass, '7.2f'))
