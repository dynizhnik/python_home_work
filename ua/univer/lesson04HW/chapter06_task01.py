def main():
    infile = open('numbers.txt', 'r')
    line = infile.readline()
    while line != '':
        num = int(line)
        print(num)
        line = infile.readline()
    infile.close()

main()