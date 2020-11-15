def main():
    file = open('number_list.txt', 'r')
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        print(line)
        line = file.readline()
    file.close()
main()