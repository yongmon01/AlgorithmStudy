n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(graph, x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(graph,i,j) == True:
            answer += 1
print(answer)


# #내답이 나은듯?

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# count = 0
#
#
# def dfs(graph, x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         for i in range(4):
#             dfs(graph, x + dx[i], y + dy[i])
#
#
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i][j] == 0:
#             count += 1
#             dfs(graph, i, j)
#
# print(count)

## bfs로도 풀었다!!!

# from collections import deque
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# count = 0
#
#
# def bfs(graph, x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         graph[x][y] = 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             elif graph[nx][ny] == 0:
#                 queue.append((nx, ny))
#
#
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i][j] == 0:
#             count += 1
#             bfs(graph, i, j)
# print(graph)
# print(count)