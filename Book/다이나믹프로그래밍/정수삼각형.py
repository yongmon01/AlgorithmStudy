n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
print(triangle)

answer_triangle = [[0] * i for i in range(1, n+1)]
answer_triangle[0][0] = triangle[0][0]
print(answer_triangle)

for i in range(1, n):
    #print('i ', i)
    current = triangle[i]
    answer_triangle[i][0] = answer_triangle[i-1][0] + triangle[i][0]
    for j in range(1, len(current)-1):
        #print('j ', j)
        answer_triangle[i][j] = max(answer_triangle[i-1][j-1], answer_triangle[i-1][j]) + triangle[i][j]
    answer_triangle[i][-1] = answer_triangle[i-1][-1] + triangle[i][-1]

print(answer_triangle)

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5