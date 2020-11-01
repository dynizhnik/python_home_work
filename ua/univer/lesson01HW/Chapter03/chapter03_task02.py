side1 = float(input('Enter 1 side of the first rectangle: '))
side2 = float(input('Enter 2 side of the first rectangle: '))
side3 = float(input('Enter 1 side of the second rectangle: '))
side4 = float(input('Enter 2 side of the second rectangle: '))

square1 = side1 * side2
square2 = side3 * side4

if side1 <= 0 or side2 <= 0 or side3 <= 0 or side4 <= 0:
    print('Please, enter side > 0!')
else:
    if square1 > square2:
        print('Square FIRST rectangle bigger and =', format(square1, '.2f'))
    elif square1 < square2:
        print('Square SECOND rectangle bigger and =', format(square2, '.2f'))
    else:
        print('Square FIRST and SECOND rectangle equal and =', format(square1, '.2f'))
