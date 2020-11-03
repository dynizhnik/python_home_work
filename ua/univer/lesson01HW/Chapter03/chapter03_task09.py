number = int(input('Enter number: '))
if number == 0:
    print('Color of number is GREEN!')
elif number in range(1,10,2) or number in range(12,19,2) or number in range(19,28,2) or number in range(30,37,2):
    print('Color of number is RED!')
elif number in range(2,11,2) or number in range(11,19,2) or number in range(20,29,2) or number in range(29,36,2):
    print('Color of number is BLACK!')
else:
    print('Incorrect number!')