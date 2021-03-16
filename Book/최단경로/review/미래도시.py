# bfs, 다익스트라, 플로이드워셜 세방법 모두가능.

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 1 to k
dist_1 = [int(1e9)] * (n+1)
# k to x
dist_2 = [int(1e9)] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k = map(int, input().split())

print(graph)

def bfs(start, dist):
    dist[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        next_node = queue.popleft()
        length = dist[next_node]
        for i in graph[next_node]:
            if dist[i] == int(1e9):
               dist[i] = length + 1
               queue.append(i)
    print(dist)

bfs(1, dist_1)
bfs(k, dist_2)

d1 = dist_1[k]
d2 = dist_2[x]
print(d1, d2)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
