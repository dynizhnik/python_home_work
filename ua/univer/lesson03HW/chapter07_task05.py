def main():
    infile = open('chapter07_task05.txt', 'r')
    number = infile.readlines()
    infile.close()

    read_index_in_file(number)

    print(number)
    bills = int(input('Enter number of bills:'))

    if bills in number:
        print('Bills found in list')
    else:
        print('Bills not found in list')

def read_index_in_file(number):
    index = 0
    while index < len(number):
        number[index] = int(number[index])
        index += 1

main()
