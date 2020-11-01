colour1 = input('Enter first main colour: ')
colour2 = input('Enter second main colour: ')
if colour1 == 'red' and colour2 == 'red':
    print('Result colour is red.')
elif colour1 == 'blue' and colour2 == 'blue':
    print('Result colour is blue.')
elif colour1 == 'yellow' and colour2 == 'yellow':
    print('Result colour is yellow.')
elif colour1 == 'red' and colour2 == 'blue' or colour2 == 'red' and colour1 == 'blue':
    print('Result colour is violet.')
elif colour1 == 'red' and colour2 == 'yellow' or colour2 == 'red' and colour1 == 'yellow':
    print('Result colour is orange.')
elif colour1 == 'yellow' and colour2 == 'blue' or colour2 == 'yellow' and colour1 == 'blue':
    print('Result colour is green.')
else:
    print('Error!')