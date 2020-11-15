def main():
    LINE = 5
    file_name = input('Enter file name: ')
    infile = open(file_name, 'r')
    line = infile.readline()
    for i in range(1, LINE + 1):
        line = line.rstrip('\n')
        if line != '':
            print(line)
        else:
            return 
        line = infile.readline()
    infile.close()

main()
