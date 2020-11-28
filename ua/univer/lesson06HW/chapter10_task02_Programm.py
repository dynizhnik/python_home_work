from ua.univer.lesson06HW.chapter10_task02_Car import Car


def main():
    DIFFERENCE = 5
    COUNT = 5
    year_model = ''
    make = ''
    speed = 0

    car = Car(year_model, make, speed)
    for count in range(COUNT):
        car.set_accelerate(differance=DIFFERENCE)
        print('Speed now is', car.get_speed())

    for count in range(COUNT):
        car.set_break(differance=DIFFERENCE)
        print('Speed now is', car.get_speed())


main()
