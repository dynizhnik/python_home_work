def main():
    file = open('numbers.txt', 'r')
    total = 0
    line = file.readline()
    while line != '':
        line = line.rstrip('\n')
        line = int(line)
        total = total + line
        line = file.readline()
    print(total)
    file.close()

main()