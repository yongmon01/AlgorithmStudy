# 다익스트라도 가능

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
#
# # 노드의 개수, 간선의 개수를 입력받기
# n, m = map(int, input().split())
#
# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# graph_1 = [[] for i in range(n + 1)]
# graph_2 = [[] for i in range(n + 1)]
# # 최단 거리 테이블을 모두 무한으로 초기화
# distance_1 = [INF] * (n + 1)
# distance_2 = [INF] * (n + 1)
#
# # 모든 간선 정보를 입력받기
# for _ in range(m):
#     a, b = map(int, input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph_1[a].append((b, 1))
#     graph_1[b].append((a,1))
#     graph_2[a].append((b, 1))
#     graph_2[b].append((a, 1))
#
# def dijkstra(start, graph, distance):
#     q = []
#     # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q: # 큐가 비어있지 않다면
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
#         if distance[now] < dist:
#             continue
#         # 현재 노드와 연결된 다른 인접한 노드들을 확인
#         for i in graph[now]:
#             cost = dist + i[1]
#             # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# start = 1
# X, K = map(int, input().split())
#
# # 다익스트라 알고리즘을 수행
# dijkstra(start, graph_1, distance_1)
# dist1 = distance_1[K]
#
# # ...
#
# dijkstra(K, graph_2, distance_2)
# dist2 = distance_2[X]
#
# print(distance_1)
# print(distance_2)
# print('d1', dist1)
# print('d2', dist2)
#
# [1000000000, 0, 1, 1, 1, 2]
# [1000000000, 1, 1, 1, 0, 1]


# 플로이드 워셜

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B 그리고 B에서 A로 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

print(graph)
if graph[1][K] == INF or graph[K][X] == INF:
    print(-1)
else:

    print(graph[1][K] + graph[K][X])

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5


# 4 2
# 1 3
# 2 4
# 3 4