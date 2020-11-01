from ua.univer.lesson02.task_class02 import print_odd
from ua.univer.lesson02.task_class03 import t03_print_asc_a_to_b, t02_input_and_print_n_k, print_10_value

while True:
    print('1. first task')
    print('2. second task')
    print('3. task 3')
    print('4. task 4')
    print('0. exit')
    answer = int(input('choise task number:'))
    if answer == 1:
        start = int(input('enter start'))
        end = int(input('enter end'))
        print_odd(start,end)
    elif answer == 2:
        t02_input_and_print_n_k()
    elif answer == 3:
        a =input('a')
        b=input('b')
        t03_print_asc_a_to_b(a,b)
    elif answer == 4:
        start = int(input('start'))
        step = int(input('step'))
        print_10_value(start, step)
    elif answer == 0:
        break
    else:
        print('error choise')

