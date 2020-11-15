arr = [2, 3, 35, 5, 9, 3, 4, 4, ]
count = 0
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        count += 1
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)
print(count)
