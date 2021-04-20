# 이 풀이가 적절한 풀이.

from collections import deque
n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, a, b = map(int, input().split())
q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], 0, i, j))
q.sort()
q = deque(q) ###

print(graph)
print(q)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(q, graph):

    while q:
        num, t, x, y = q.popleft()
        if t == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = num
                q.append((num, t+1, nx, ny))

bfs(q, graph)
print(graph)
print(graph[a-1][b-1])