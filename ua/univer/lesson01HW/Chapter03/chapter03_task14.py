weight = int(input('Enter your weight in kg: '))
growth = float(input('Enter your growth in m: '))
IMT = weight / growth
MIN_IMT = 18.5
MAX_IMT = 25
if IMT < MIN_IMT:
    print('Your IMT is: ', format(IMT, '.1f'))
    print('You have small weight.')
elif IMT >= MIN_IMT and IMT <= MAX_IMT:
    print('Your IMT is: ', format(IMT, '.1f'))
    print('You have normal weight.')
elif IMT > MAX_IMT:
    print('Your IMT is: ', format(IMT, '.1f'))
    print('You have big weight.')
else:
    print('Error count.')