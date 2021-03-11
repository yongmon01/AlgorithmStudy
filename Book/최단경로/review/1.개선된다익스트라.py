import heapq
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (n+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        d, now = heapq.heappop(queue)
        for node, dist in graph[now]:
            if d + dist < distance[node]:
                distance[node] = d + dist
                heapq.heappush(queue, (distance[node], node))

dijkstra(start)
print(graph)
print(distance)