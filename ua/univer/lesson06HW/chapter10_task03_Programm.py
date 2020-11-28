from ua.univer.lesson06HW.chapter10_task03_Information import Information


def main():
    list = make_list()
    print('Your information:')
    display_list(list)


def make_list():
    peoples = []
    for count in range(3):
        name = input(f'Enter {count + 1} name:')
        address = input(f'Enter {count + 1} address:')
        age = int(input(f'Enter {count + 1} age:'))
        phone = int(input(f'Enter {count + 1} phone:'))
        people = Information(name, address, age, phone)
        peoples.append(people)
    return (peoples)


def display_list(peoples):
    for people in peoples:
        print(people.get_name())
        print(people.get_address())
        print(people.get_age())
        print(people.get_phone())
        print()


main()
