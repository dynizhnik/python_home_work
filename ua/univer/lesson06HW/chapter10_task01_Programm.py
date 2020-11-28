from ua.univer.lesson06HW.chapter10_task01_Pet import Pet


def main():
    name = input('Enter name your pet: ')
    animal_type = input('Enter type your pet: ')
    age = float(input('Enter age your pet: '))

    pet = Pet(name, animal_type, age)

    print('Pet name is', pet.get_name(), ', pet type is', pet.get_animal_type(), 'and pet age is', pet.get_age())

main()