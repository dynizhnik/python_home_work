FILENAME = "messages.txt"

my_list = list()

with open(FILENAME, "r") as file:
    for i in range(6):
        contents = file.readlines()
        string += contents[i]
    