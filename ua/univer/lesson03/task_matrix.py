if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [6, 7, 8, 9, 4, 7],
        [3, 4, 5, 6, 5]
    ]
    print(len(matrix))
    print(len(matrix[0]))
    print(len(matrix[1]))
    print(len(matrix[2]))
    sum_matrix = 0

    for i in range(len(matrix)):
        # ---befor i row
        # ---
        for j in range(len(matrix[i])):
            # ---for each j cell i row
            sum_matrix += 1
            if matrix[i][j] % 2 == 0:
                print(matrix[i][j], end='\t')
            else:
                print('-', end='\t')
            # ---
        # ---after row
        print()
        print('Sum row: ', sum_matrix)
    print('Sum: ', sum_matrix)