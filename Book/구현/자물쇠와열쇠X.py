key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

n = len(lock)
m = len(key)

def rotate_right(matrix): #직사각형도?
    rotated_matrix = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[n-1-j][i]
    return rotated_matrix

new_lock = [[-1]*n*3 for _ in range(3*n)]
for i in range(n):
    for j in range(n):
        new_lock[i+n][j+n] = lock[i][j]

def check(matrix):
    for i in range(len(matrix)//3, (len(matrix)//3)*2):
        for j in range(len(matrix)//3, (len(matrix)//3)*2):
            if matrix[i][j] != 1:
                return False
    return True

for rotate in range(4):
    key = rotate_right(key)
    for i in range(2*n):
        for j in range(2*n):
            for x in range(m):
                for y in range(m):
                    new_lock[i+x][j+y] += key[x][y]
            if check(new_lock) is True:
                print(True)
            for x in range(m):
                for y in range(m):
                    new_lock[i+x][j+y] -= key[x][y]

