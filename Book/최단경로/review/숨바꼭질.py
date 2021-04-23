# 전형적인 다익스트라 문제.

import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)
distance[1] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, (0, 1))
while q:
    d, node = heapq.heappop(q)
    if distance[node] < d:
        continue
    for node2, d2 in graph[node]:
        if distance[node2] > d + d2:
            distance[node2] = d + d2
            heapq.heappush(q, (distance[node2], node2))

print(distance)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 5 4
# 5 2