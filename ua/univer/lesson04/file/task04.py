FILENAME = "messages.txt"
arr_int = []
for i in range(6):
    arr_int.append(int(input('enter int :')))

with open(FILENAME, "r") as file_data:
    for line in arr_int:
        arr_int.append(int(line))
        print(arr_int)