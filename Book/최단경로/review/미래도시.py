# bfs, 다익스트라, 플로이드워셜 세방법 모두가능.
### 아..! bfs를 최단경로 문제로 풀때는 거리들이 모두 1일때만 가능..! ###

# 다익스트라 방법
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k = map(int, input().split())

dist_1 = [int(1e9)] * (n+1)
dist_2 = [int(1e9)] * (n+1)
dist_1[1] = 0
dist_2[k] = 0

def dijkstra(start, dist):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        d, node = heapq.heappop(queue)
        if dist[node] < d:
            continue
        for i in graph[node]:
            if dist[i] > d + 1:
                dist[i] = d + 1
                heapq.heappush(queue, (dist[i], i))

dijkstra(1, dist_1)
print(dist_1)
dijkstra(k, dist_2)
print(dist_2)

print(dist_1[k], dist_2[x])




# 플로이드 워셜 방법
# n, m = map(int, input().split())
# graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
# x, k = map(int, input().split())
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             if graph[j][k] > graph[j][i] + graph[i][k]:
#                 graph[j][k] = graph[j][i] + graph[i][k]
#
# print(graph)
# print(graph[1][k], graph[k][x])


# bfs 방법
# from collections import deque
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
#
# # 1 to k
# dist_1 = [int(1e9)] * (n+1)
# # k to x
# dist_2 = [int(1e9)] * (n+1)
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# x, k = map(int, input().split())
#
# print(graph)
#
#
# def bfs(start, dist):
#     dist[start] = 0
#     queue = deque()
#     queue.append(start)
#     while queue:
#         next_node = queue.popleft()
#         length = dist[next_node]
#         for i in graph[next_node]:
#             if dist[i] == int(1e9):
#                dist[i] = length + 1
#                queue.append(i)
#     print(dist)
#
#
# bfs(1, dist_1)
# bfs(k, dist_2)
#
# d1 = dist_1[k]
# d2 = dist_2[x]
# print(d1, d2)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
