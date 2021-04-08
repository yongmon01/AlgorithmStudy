import heapq
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (n+1)
distance[start] = 0
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, start))

while q:
    d, node = heapq.heappop(q)
    if distance[node] < d:
        continue
    for node2, d2 in graph[node]:
        if d2 + distance[node] < distance[node2]:
            distance[node2] = d2 + distance[node]
            heapq.heappush(q, (distance[node2], node2))

print(graph)
print(distance)




# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2