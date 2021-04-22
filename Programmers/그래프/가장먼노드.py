# 다익스트라 풀이
import heapq
def dikjstra(graph, distance):
    q = [] #
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

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    distance = [int(1e9)] * (n+1)
    distance[0] = -1
    distance[1] = 0
    for i in edge:
        graph[i[0]].append((i[1], 1))
        graph[i[1]].append((i[0], 1))
    print(graph)

    dikjstra(graph, distance)

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)
