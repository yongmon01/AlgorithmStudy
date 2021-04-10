from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

count = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# def dfs(x,y):
#
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >= 0 and ny >= 0 and nx < n and ny < m:
#                 dfs(nx, ny)

def bfs(x,y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        graph[a][b] = 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(i, j)
            count += 1
            bfs(i,j)

print(graph)
print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000


# from collections import deque
#
# # 세로길이 n 가로길이 m
# n, m = map(int, input().split())
# graph = []
#
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# count = 0
#
# def bfs(a,b):
#     queue = deque()
#     queue.append((a,b))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >=0 and ny>=0 and nx < n and ny < m and graph[nx][ny] == 0:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = 1
#
# def dfs(a,b):
#     if a <0 or b<0 or a>= n or b>=m:
#         return
#     if graph[a][b] == 0:
#         graph[a][b] = 1
#         for i in range(4):
#             dfs(a+dx[i], b+dy[i])
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             count += 1
#             dfs(i, j)
#
# print(graph)
# print(count)
#
# # 4 5
# # 00110
# # 00011
# # 11111
# # 00000