age = int(input('Please, enter your age:'))

if age <= 0:
    print('Please, enter number >0!')
elif age > 0 and age <= 1:
    print('You are baby!')
elif age > 1 and age < 13:
    print('You are child!')
elif age >= 13 and age < 20:
    print('You are teenager!')
elif age >= 20:
    print('You are adult!')
