import heapq

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))

distance = [int(1e9)] * (n+1)
distance[c] = 0

def dijkstra(start, dist):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        d1, node = heapq.heappop(queue)
        if dist[node] < d1:
            continue
        for node2, d2 in graph[node]:
            if dist[node2] > d2 + d1:
                dist[node2] = d2 + d1
                heapq.heappush(queue, (dist[node2], node2))

dijkstra(c, distance)
print(distance)
count = 0
max_time = 0

for i in distance:
    if i != 0 and i != int(1e9):
        count += 1
    if i > max_time and i != int(1e9):
        max_time = i

print('count ', count, 'max time ', max_time)