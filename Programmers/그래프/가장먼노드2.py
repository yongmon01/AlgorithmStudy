# bfs 풀이
from collections import deque
def bfs(graph, distance):
    visited = [False] * (n+1)
    visited[1] = True
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] is False:
                distance[i] = distance[node] + 1
                q.append(i)
                visited[i] = True
    print(distance)

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    distance = [0] * (n+1)
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    print(graph)

    bfs(graph, distance)

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)