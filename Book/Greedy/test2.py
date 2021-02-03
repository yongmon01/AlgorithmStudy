import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    # a 에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
print(graph)






# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
#
# for i in range(m):
#     # a 에서 b로 가는 비용 c
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# queue = []
# distance[start] = 0
# heapq.heappush(queue, (0, start))
# while queue:
#     dist, now = heapq.heappop(queue)
#
#     if distance[now] < dist:
#         continue
#
#     for i in graph[now]:
#         if distance[i[0]] > i[1] + distance[now]:
#             distance[i[0]] = i[1] + distance[now]
#             heapq.heappush(queue, (distance[i[0]], i[0]))
#
# print(distance)







# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
#
# for i in range(m):
#     # a 에서 b로 가는 비용 c
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# def return_next_index():
#     min_dist = INF
#     index = 1
#     for i in range(1, n+1):
#         if visited[i] is False and distance[i] < min_dist:
#             min_dist = distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     visited[start] = True
#     distance[start] = 0
#     for node in graph[start]:
#         distance[node[0]] = node[1]
#     for _ in range(n-1): # n?
#         index = return_next_index()
#         print(index)
#         visited[index] = True
#         for node in graph[index]:
#             if distance[node[0]] > distance[index] + node[1]:
#                 distance[node[0]] = distance[index] + node[1]
#
# dijkstra(1)
# print(distance)