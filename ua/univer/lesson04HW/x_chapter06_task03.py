def main():
    file = open('number_list.txt', 'w')
    for i in range (1,101):
        line = file.writelines(str(i) + '\n')
    file.close()

main()