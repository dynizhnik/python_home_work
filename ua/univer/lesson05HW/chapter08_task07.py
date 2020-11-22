def main():
    file = open('text.txt', 'r')
    line = file.readline()
    big_boolean = False
    big = 0
    small = 0
    number = 0
    space = 0
    while line != '':
        line = line.rstrip('\n')
        for word in line:
            if word.isupper():
                big += 1
            if word.islower():
                small += 1
            if word.isdigit():
                number += 1
            if word.isspace():
                space += 1
        print(line)
        line = file.readline()
    print('In this files is', big, 'big words')
    print('In this files is', small, 'small words')
    print('In this files is', number,'number words')
    print('In this files is', space, 'space words')
    file.close()


main()
