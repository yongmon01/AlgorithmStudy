from collections import deque

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
target_s, target_x, target_y = map(int, input().split())

queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((graph[i][j], 0, i, j))
queue.sort()
queue = deque(queue)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while queue:
    virus, s, x, y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])




from collections import deque

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
target_s, target_x, target_y = map(int, input().split())
print(graph)

queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((graph[i][j], 0, i, j))
queue.sort()
queue = deque(queue)
print(queue)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while queue:
    virus, s, x, y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            graph[nx][ny] = virus
            queue.append((virus, s+1, nx, ny))

print('answer: ', graph)
print(graph[target_x-1][target_y-1])








# # pypy ok.. python3 시간초과 ############################ my solution2
#
# from collections import deque
# import sys
# import time
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
# print(graph)
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] != 0:
#             graph[i][j] = [graph[i][j], 0]
#
# print(graph)
#
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
#
# def bfs(graph,x,y):
#     # value = graph[x][y][0]
#     # length = graph[x][y][1]
#
#     visited = [[False] * n for _ in range(n)]
#     visited[x][y] = True
#
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         print(queue) #
#         a, b = queue.popleft()
#         value = graph[a][b][0]
#         length = graph[a][b][1]
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx >= 0 and nx < n and ny >= 0 and ny < n:
#                 # 한번도 된적없으면 무조건
#                 if graph[nx][ny] == 0 and visited[nx][ny] == False:
#                     graph[nx][ny] = [value, length+1]
#                     queue.append((nx, ny))
#                     visited[nx][ny] = True
#                 # 전염 불가
#                 elif graph[nx][ny][1] == 0:
#                     continue
#                 # 전염가능
#                 elif graph[nx][ny][1] > length + 1 and visited[nx][ny] == False:
#                     graph[nx][ny] = [value, length+1]
#                     queue.append((nx, ny))
#                     visited[nx][ny] = True
#                 elif graph[nx][ny][1] == length + 1 and graph[nx][ny][0] > value and visited[nx][ny] == False:
#                     graph[nx][ny] = [value, length+1]
#                     queue.append((nx, ny))
#                     visited[nx][ny] = True
#     print('after bfs', graph)
#
# for i in range(n):
#     for j in range(n):
#         print(i,j,'....')
#         if graph[i][j] != 0 and graph[i][j][1] == 0:
#             bfs(graph, i, j)
#
# # bfs(graph,0,0)
# print(graph)
#
# print('answer: ')
# print(graph[x-1][y-1][0])


# # 졌잘싸...         ######################################## my solution 1
#
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
# print(graph)
#
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
#
# for t in range(s):
#
#     new_graph = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             new_graph[i][j] = graph[i][j]
#
#     for i in range(n):
#         for j in range(n):
#             v_num = graph[i][j]
#             if v_num == 0:
#                 continue
#             for p in range(4):
#                 nx = i + dx[p]
#                 ny = j + dy[p]
#                 if nx >=0 and nx < n and ny >=0 and ny < n:
#                     if new_graph[nx][ny] == 0:
#                         new_graph[nx][ny] = v_num
#                     elif new_graph[nx][ny] > v_num and graph[nx][ny] == 0:
#                         new_graph[nx][ny] = v_num
#     graph = new_graph
#     print(graph)
#
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2
