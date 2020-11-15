import os

def main():
    NAME = 'Джон Перц'
    found = False
    file = open('students.txt', 'r')
    temp = open('temp.txt', 'w')
    name = file.readline()
    mark = file.readline()
    while name != '':
        name = name.rstrip('\n')
        if name != NAME:
            temp.write(name + '\n')
            temp.write(mark)
            name = file.readline()
            mark = file.readline()
        else:
            found = True
            name = file.readline()
            mark = file.readline()
    file.close()
    temp.close()
    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if found:
        print('File update.')
    else:
        print('No this student.')

main()