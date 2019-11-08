

def initialize_matrix(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    return matrix


def is_safe(matrix, i, j, length):
    print((i, j))
    for k in range(0, length):
        if i-k >= 0 and j-k >= 0:
            if matrix[i-k][j-k] == 1:
                return False
        if i-k >= 0 and j+k < length:
            if matrix[i-k][j-k] == 1:
                return False
        if i+k < length and j-k >= 0:
            if matrix[i+k][j-k] == 1:
                return False
        if i+k < length and j+k < length:
            if matrix[i+k][j+k] == 1:
                return False
        if matrix[i][k] == 1:
            return False
        if matrix[k][j] == 1:
            return False
    return True


def backtracking(matrix, col):
    length = len(matrix)
    if col >= length:
        return True
    for i in range(0, length):
        if is_safe(matrix, i, col, length):
            matrix[i][col] = 1
            if backtracking(matrix, col + 1):
                return True
            matrix[i][col] = 0
        for j in range(0, length):
            for k in range(0, length):
                print(matrix[j][k], end=' ')
            print()
    print("Am ajuns aici")
    return False


if __name__ == '__main__':
    backtracking(initialize_matrix(4), 0)

