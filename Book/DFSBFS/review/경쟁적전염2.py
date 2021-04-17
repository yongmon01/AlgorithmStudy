# 이 풀이는 bfs를 끝까지 진행한 풀이.. / s초 후라는 것을 고려하지못함..

from collections import deque
n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, a, b = map(int, input().split())
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            graph[i][j] = (graph[i][j],0)
print(graph)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, x, y):

    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        num, time = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = (num, time + 1)
                    q.append((nx, ny))
                elif graph[nx][ny][1] > time + 1:
                    graph[nx][ny] = (num, time + 1)
                    q.append((nx, ny))
                elif graph[nx][ny][1] == time + 1 and graph[nx][ny][0] > num:
                    graph[nx][ny] = (num, time + 1)
                    q.append((nx, ny))

for i in range(n):
    for j in range(n):
        bfs(graph,i,j)
print(graph)
print(graph[a-1][b-1][0])