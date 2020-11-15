def main():
    total = 0
    file = open('number_list.txt', 'r')
    line = file.readline()
    while line != '':
        line = int(line)
        total = total + line
        line = file.readline()
    file.close()
    print(total)
main()