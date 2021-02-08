# 나의 bfs 풀이 !
from collections import deque
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
print(matrix)

answer = [[0] * n for _ in range(n)]
answer[0][0] = matrix[0][0]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(a,b):
    queue = deque()
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx <n and ny >=0 and ny < n:
                if answer[nx][ny] == 0:
                    answer[nx][ny] = answer[x][y] + matrix[nx][ny]
                    queue.append((nx, ny))
                elif answer[x][y] + matrix[nx][ny] < answer[nx][ny]:
                    answer[nx][ny] = answer[x][y] + matrix[nx][ny]
                    queue.append((nx, ny))

dfs(0, 0)
print(answer)

# # 다이나믹 프로그래밍 처럼 풀었는데 맞는듯한데 왜 틀릴까...
# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# print(matrix)
#
# answer = [[0] * n for _ in range(n)]
# print(answer)
#
# answer[0][0] = matrix[0][0]
#
# for i in range(1, n):
#     print(i)
#     answer[0][i] = answer[0][i-1] + matrix[0][i]
#     answer[i][0] = answer[i-1][0] + matrix[i][0]
#
# print(answer)
#
# for i in range(1,n):
#     for j in range(1,n):
#         answer[i][j] = min(answer[i-1][j], answer[i][j-1]) + matrix[i][j]
#
# print(answer)


# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
