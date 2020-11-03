POINT_0 = 0
POINT_5 = 5
POINT_15 = 15
POINT_30 = 30
POINT_60 = 60

count = int(input('Enter count of book that you bought: '))
if count in range(0,2):
    print(f'Your score is {POINT_0}')
elif count in range(2,4):
        print(f'Your score is {POINT_5}')
elif count in range(4, 6):
    print(f'Your score is {POINT_15}')
elif count in range(6,8):
        print(f'Your score is {POINT_30}')
elif count >= 8:
    print(f'Your score is {POINT_60}')
else:
    print('Error count!')