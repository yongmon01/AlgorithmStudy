from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        length = graph[a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = length + 1

bfs(0,0)
print(graph)


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
#
# visited = [[False] * m for _ in range(n)]
#
# def bfs(a,b):
#     queue = deque()
#     queue.append((a,b))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >=0 and ny>=0 and nx < n and ny < m and graph[nx][ny] != 0 and visited[nx][ny] is False:
#                 queue.append((nx, ny))
#                 visited[nx][ny] = True
#                 graph[nx][ny] = graph[x][y]+1
#
# bfs(0, 0)
#
# print(visited)
# print(graph)
#
# # 5 6
# # 101010
# # 111111
# # 000001
# # 111111
# # 111111

