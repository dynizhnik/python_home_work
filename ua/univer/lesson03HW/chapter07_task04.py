def main():

    NUM = 20
    list = []


    enter_list(NUM, list)
    sum_and_average_list(list)

    print('Minimum number in list is:', min(list))
    print('Maximum number in list is:', max(list))

def enter_list(NUM, list):
    for i in range(NUM):
        list.append(int(input(f'Enter {i+1} number: ')))
    return list

def sum_and_average_list(list):
    total = 0
    for number in list:
        total += number
        average = total / len(list)
    print('Total counts is:', total)
    print('Average counts is:', average)


main()