def main():
    list = []

    enter_list(list)
    n = int(input('Enter count n:'))
    find_count_more_n(list, n)

def enter_list(list):
    again = 'y'
    while again == 'y':
        name = int(input('Enter count of list: '))
        list.append(name)
        print('Do you want enter new count?')
        again = input('y or n:')

def find_count_more_n(list, n):
    for i in range(len(list)):
        if n < list[i]:
            print(list[i])


main()
