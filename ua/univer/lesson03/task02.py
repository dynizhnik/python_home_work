import random


def get_list_odd_even():
    global list_odd, list_even
    list_odd = []
    list_even = []
    for i in range(10):
        value = int(input(f'Enter count {i}: '))
        if value % 2 == 0:
            list_even.append(value)
        else:
            list_odd.append(value)


get_list_odd_even()


def print_list_odd_even():
    print(list_even)
    print(list_odd)

print_list_odd_even()

print(len(list_even))
print(len(list_odd))


print(print_list_odd_even())


def get_list_10_int():
    return list(random.sample(list(range(1,10)),10))

get_list_10_int()