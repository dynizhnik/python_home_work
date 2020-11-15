def main():
    file = open('names.txt', 'r')
    total = 0
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        total = total + 1
        line = file.readline()
    print(total)
    file.close()

main()
