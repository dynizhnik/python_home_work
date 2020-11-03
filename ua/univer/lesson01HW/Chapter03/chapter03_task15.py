MIN = 60
HOU = 3600
DAY = 86400

sec = int(input('Enter count of seconds: '))
if sec > 0:
    day = sec // DAY
    hour = (sec - DAY * day) // HOU
    minute = (sec - DAY * day - HOU * hour) // MIN
    seconnd = sec % MIN
    print('Your count is: ', day, 'days', hour, 'hours', minute, 'minutes', seconnd, 'seconds')
else:
    print('Error count!')
