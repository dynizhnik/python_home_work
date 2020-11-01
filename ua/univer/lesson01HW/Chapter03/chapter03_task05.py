G = 9.8
mass = int(input('Enter your mass: '))
MIN_WEIGHT = 100
MAX_WEIGHT = 500
weight = mass * G
if weight > MAX_WEIGHT:
    print('You are overweight!')
elif weight < MIN_WEIGHT:
    print('You are very skinny!')
else:
    print('You have a good weight.')