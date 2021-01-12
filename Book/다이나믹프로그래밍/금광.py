import sys
n, m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
answer_matrix = [[0] * m for i in range(n)]
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
print(answer_matrix)

k = 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = numbers[k]
        answer_matrix[i][j] = numbers[k]
        k = k + 1
print('matrix ', matrix)

for i in range(1, m):
    for j in range(n):
        curr_nums = []
        for k in range(-1, 2, 1):
            if j + k >= 0 and j + k < n and i - 1 >= 0 and i - 1 < m:
                curr_nums.append(answer_matrix[j+k][i-1])
        answer_matrix[j][i] += max(curr_nums)
print("answer_matrix ", answer_matrix)

li = [i[-1] for i in answer_matrix]
print(max(li))
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7