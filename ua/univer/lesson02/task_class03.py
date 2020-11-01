from ua.univer.lesson02.task_class04 import start, step


def t02_print_n_k(n, k):
    for i in range(n):
        print(k)


def t02_input_and_print_n_k():
    k = int(input('Enter k'))
    n = int(input('Enter n'))
    t02_print_n_k(n, k)


t02_print_n_k(4, 100)
t02_input_and_print_n_k()


# Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.

def t03_print_asc_a_to_b(a, b):
    x = a
    count = 0
    while x <= b:
        print(x)
        x += 1
        count += 1
    print(x)


# 4
def print_10_value():
    x = start
    for i in range(10):
        print(x)
        x -= step
