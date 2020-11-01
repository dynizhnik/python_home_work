number_of_count = int(input('Enter number of count: '))
my_list = list(range(number_of_count * 2))
for x in my_list:
    if x % 2 == 1:
        print(x, end=', ')


def task01_mylist():
    global mylist
    mylist = list(range(1, 20, 2))
    print(mylist)


task01_mylist()

mylist2 = list()
for i in range(20):
    if i % 2 == 1:
        mylist2.append(i)
    print(mylist2)

