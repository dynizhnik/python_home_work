def sort_matrix(matrix):
    sum_row_list = []
    sum_row = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum_row += matrix[i]
        sum_row_list.append(sum_row)
    print(sum_row_list)
    bouble_sort(sum_row_list)
    print(sum_row_list)


def bouble_sort():
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(count)


if __name__ == '__main__':

    matrix = [[1, 2, 3, 4], [4, 3, 5, 6], [9, 7, 4, 7]]
    sort_matrix(matrix)
