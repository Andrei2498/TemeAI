import time


def show_matrix(matrix, length):
    for j in range(0, length):
        for k in range(0, length):
            if matrix[j][k] < 0:
                matrix[j][k] = 0
            print(matrix[j][k], end=' ')
        print()
    print()


def initialize_matrix(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    return matrix


def is_safe(matrix, i, j, length, value):
    for k in range(0, length):
        if i - k >= 0 and j - k >= 0:
            matrix[i-k][j-k] += value
            if matrix[i - k][j - k] == 1:
                return False
        if i - k >= 0 and j + k < length:
            matrix[i-k][j+k] += value
            if matrix[i - k][j + k] == 1:
                return False
        if i + k < length and j - k >= 0:
            matrix[i+k][j-k] += value
            if matrix[i + k][j - k] == 1:
                return False
        if i + k < length and j + k < length:
            matrix[i+k][j+k] += value
            if matrix[i + k][j + k] == 1:
                return False
        if matrix[i][k] == 1:
            return False
        else:
            matrix[i][k] += value
        if matrix[k][j] == 1:
            return False
        else:
            matrix[k][j] += value
        # matrix[i][j] = 1
    return True


def backtracking(matrix, j):
    length = len(matrix)
    if j >= length:
        return True
    for i in range(0, length):
        if matrix[j][i] == 0:
            is_safe(matrix, j, i, length, -1)
            matrix[j][i] = 1
            if backtracking(matrix, j + 1):
                return True
            is_safe(matrix, j, i, length, 1)
            matrix[j][i] = 0
    return False


if __name__ == '__main__':
    start_time = time.time()
    solution = initialize_matrix(25)
    backtracking(solution, 0)
    show_matrix(solution, 25)
    print(time.time()-start_time)
