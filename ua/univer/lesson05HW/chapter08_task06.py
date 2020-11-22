def main():
    file = open('text.txt', 'r')
    line = file.readline()
    average = 0
    count = 0
    total_words = 0
    while line != '':
        line = line.rstrip('\n')
        line = line.split(' ')
        average = len(line)
        count += 1
        total_words += average
        print('In', count, 'sentence', average, 'words')
        line = file.readline()
    print('Total sentences is: ', count)
    print('Total average words is: ', float(format(total_words / count, '.1f')))
    file.close()


main()
