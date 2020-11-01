day = int(input('Enter a day of month: '))
month = int(input('Enter month in number format: '))
year = int(input('Enter year in 2 number format'))
composition = day * month
count = composition - year
if day in range(1, 32) and month in range(1, 13) and year in range(1, 100) and count == 0:
    print('Magic date!')
elif day in range(1, 32) and month in range(1, 13) and year in range(1, 100) and count != 0:
    print('It`s not magic date!')
else:
    print('Error! Enter correct count.')
