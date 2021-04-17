# 1초 마다 한번씩 계산하는 방법. 정답은 맞는듯하나 시간초과.

import copy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
graph2 = copy.deepcopy(graph)

for _ in range(s):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                for c in range(4):
                    nx = i + dx[c]
                    ny = j + dy[c]
                    if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] == 0:
                        if graph2[nx][ny] == 0:
                            graph2[nx][ny] = graph[i][j]
                        else:
                            graph2[nx][ny] = min(graph2[nx][ny], graph[i][j])
    graph = copy.deepcopy(graph2)

# print(graph)
# print(graph2)
print(graph[x-1][y-1])

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2