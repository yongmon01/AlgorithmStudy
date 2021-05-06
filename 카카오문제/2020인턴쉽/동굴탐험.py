# 효율성에서 반은 실패했지만 나름 좋은 아이디어였다.. 잘했다.

from collections import deque
def solution(n, path, order):
    if 0 in [i[1] for i in order]:
        return False

    answer = True
    times = [0] * n #
    visited = [False] * n
    all_visited = [False] * n
    previous = [[] for _ in range(n)]
    for i in range(len(order)):
        previous[order[i][1]].append(order[i][0])
    print('prev', previous)

    graph = [[] for _ in range(n)]
    for i in range(len(path)):
        graph[path[i][0]].append(path[i][1])
        graph[path[i][1]].append(path[i][0])
    print(graph)

    q = deque()
    q.append(0)

    prev = -1
    while q:
        node = q.popleft()
        times[node] += 1
        if times[node] > n:
            return False
        if prev == node:
            return False
        prev = node
        visited[node] = True
        for nd in graph[node]:
            if len(previous[nd]) != 0:
                necess = previous[nd][0]
                if visited[necess] and not visited[nd]:
                    q.append(nd)
            elif not visited[nd]:
                q.append(nd)

        if all_visited[node] is True:
            continue
        if not is_all_visited(node, graph, visited, all_visited):
            q.append(node)

    return True

def is_all_visited(node, graph, visited, all_visited):

    for i in graph[node]:
        if not visited[i]:
            return False
    all_visited[node] = True
    return True

print(solution(2, [[0,1]],[[0,1]]))
#print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))

# import time
# from collections import deque
# def solution(n, path, order):
#     answer = True
#     times = [0] * n #
#     visited = [False] * n
#     all_visited = [False] * n
#
#     graph = [[] for _ in range(n)]
#     for i in range(len(path)):
#         graph[path[i][0]].append(path[i][1])
#         graph[path[i][1]].append(path[i][0])
#     print(graph)
#
#     q = deque()
#     q.append(0)
#
#     prev = -1
#     while q:
#         node = q.popleft()
#         times[node] += 1
#         if times[node] > n:
#             return False
#         if prev == node:
#             return False
#         prev = node
#         # print(node)
#         # time.sleep(0.5)
#         visited[node] = True
#         for nd in graph[node]:
#             if nd in [i[1] for i in order]:
#                 index = [i[1] for i in order].index(nd)
#                 necess = order[index][0]
#                 if visited[necess] and not visited[nd]:
#                     del order[index] #
#                     q.append(nd)
#             elif not visited[nd]:
#                 q.append(nd)
#
#         if all_visited[node] is True:
#             continue
#         if not is_all_visited(node, graph, visited, all_visited):
#             q.append(node)
#
#     return True
#
# def is_all_visited(node, graph, visited, all_visited):
#
#     for i in graph[node]:
#         if not visited[i]:
#             return False
#     all_visited[node] = True
#     return True
#
#
#
# print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))