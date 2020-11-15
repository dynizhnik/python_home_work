def main():
    count = 0
    file_name = input('Enter file name: ')
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        count = count + 1
        print('Line #', count, ': ', line, sep='')
        line = file.readline()
    file.close()

main()
