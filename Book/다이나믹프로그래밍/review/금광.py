n, m = map(int, input().split())
numbers = list(map(int, input().split()))
matrix = []
for i in range(0, len(numbers)-1, 4):
    matrix.append(numbers[i:i+4])
print(matrix)

for i in range(1, m):
    for j in range(n):
        a, b, c = 0, 0, 0
        #왼위
        if j-1 >= 0:
            a = matrix[j-1][i-1]
        #왼
        b = matrix[j][i-1]
        #왼아래
        if j + 1 < n:
            c = matrix[j+1][i-1]
        matrix[j][i] = max(a,b,c) + matrix[j][i]

print(matrix)

answer = 0
for i in range(m):
    answer = max(answer, matrix[i][-1])
print(answer)

# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7

# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2