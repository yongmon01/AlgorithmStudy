# 전에 dp 풀이는 아래 와 오른쪽에서 오는경우를 생각못함.

from collections import deque
import time
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
answer = [[0] * n for _ in range(n)]
answer[0][0] = graph[0][0]
print(graph)
print(answer)

dx, dy = [-1, 0, 1, 0], [0,1,0,-1]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if answer[nx][ny] == 0:
                    answer[nx][ny] = answer[x][y] + graph[nx][ny]
                    q.append((nx, ny))
                elif answer[nx][ny] > answer[x][y] + graph[nx][ny]:
                    answer[nx][ny] = answer[x][y] + graph[nx][ny]
                    q.append((nx, ny))
    print(answer)

bfs(0,0)

# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5