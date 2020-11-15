def main():
    file = open('numbers.txt', 'r')
    total = 0
    count = 0
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        line = int(line)
        total = total + line
        count = count + 1
        line = file.readline()
    print('Average :', format(total/count, '.2f'))
    file.close()
main()