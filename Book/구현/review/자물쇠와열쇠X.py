# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# def rotate(matrix):
#     rotated_matrix = [[-1] * len(matrix) for _ in range(len(matrix))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             rotated_matrix[i][j] = matrix[len(matrix)-1-j][i]
#     return rotated_matrix
#
# def isMatch(matrix, m, n):
#     for i in range(n-1, m+n-1):
#         for j in range(n-1, m+n-1):
#             if matrix[i][j] != 1:
#                 return False
#     return True
#
# def put_lock(lock, m, n):
#     matrix = [[-101] * (m + 2 * n - 2) for _ in range(m + 2 * n - 2)]
#     for i in range(n):
#         for j in range(n):
#             matrix[m+i-1][m+j-1] = lock[i][j]
#     return matrix
#
# def solution(key, lock):
#     m = len(key)
#     n = len(lock)
#     match = False
#
#     for _ in range(4):
#         matrix = put_lock(lock, m, n)
#         # print('put_lock', matrix)
#         for p in range(m + n -1):
#             for q in range(m + n -1):
#                 for i in range(m):
#                     for j in range(m):
#                         matrix[p+i][q+j] = matrix[p+i][q+j] + key[i][j]
#                         # print(p,q,i,j)
#                         # print(p+i, q+j)
#                         # print(matrix)
#                 # print('matrixx', matrix)
#                 match = isMatch(matrix, m, n)
#                 if match is True:
#                     return True
#                 for i in range(m):
#                     for j in range(m):
#                         matrix[p+i][q+j] = matrix[p+i][q+j] - key[i][j]
#         key = rotate(key)
#     return match
#
# key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(solution(key, lock))


# matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(matrix):
    rotated_matrix = [[-1] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            rotated_matrix[i][j] = matrix[len(matrix)-1-j][i]
    return rotated_matrix

def isMatch(matrix, m, n):
    for i in range(n-1, m+n-1):
        for j in range(n-1, m+n-1):
            if matrix[i][j] != 1:
                return False
    return True

def put_lock(lock, m, n):
    matrix = [[-101] * (m + 2 * n - 2) for _ in range(m + 2 * n - 2)]
    for i in range(n):
        for j in range(n):
            matrix[m+i-1][m+j-1] = lock[i][j]
    return matrix

def solution(key, lock):
    m = len(key)
    n = len(lock)
    match = False

    for _ in range(4):
        matrix = put_lock(lock, m, n)
        print('put_lock', matrix)
        for p in range(m + n -1):
            for q in range(m + n -1):
                for i in range(m):
                    for j in range(m):
                        matrix[p+i][q+j] = matrix[p+i][q+j] + key[i][j]
                        # print(p,q,i,j)
                        # print(p+i, q+j)
                print(p, matrix)
                match = isMatch(matrix, m, n)
                if match is True:
                    return True
                matrix = put_lock(lock, m, n)
        key = rotate(key)
    return match

key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))


