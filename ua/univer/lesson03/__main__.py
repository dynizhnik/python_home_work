if __name__ == '__main__':

    mylist = [1, 2, 3, 4, 5, 6, 78, 89]
    print(mylist[0])
    mylist[0] = 11
    print(mylist[0])

    print(mylist)
    print()

    for x in mylist:
        print(x)
    print()

    for i in range(0, 6, 1):
        print('mylist[', i, '] = ', mylist[i])

    print()

    for i in range(0, len(mylist), 1):
        print('mylist[', i, '] = ', mylist[i])


print("Task1")
print("Task2")
print("Task3")
print("Task4")