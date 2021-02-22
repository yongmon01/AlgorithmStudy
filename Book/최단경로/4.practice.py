import sys
import heapq
input = sys.stdin.readline
# 노드, 간선
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 맞나 긴가민가..
def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        for i in graph[now]:
            # if dist + i[1] < distance[i[0]]:
            if distance[now] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[now] + i[1]
                heapq.heappush(queue, (distance[i[0]], i[0]))
dijkstra(start)
print(graph)
print(distance)