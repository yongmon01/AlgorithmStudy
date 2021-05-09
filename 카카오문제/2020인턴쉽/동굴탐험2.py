# 와... 딕셔너리 이용해서 시간복잡도를 이런방법으로 줄일수있구나 대박

from collections import deque

def solution(n, path, order):
    # 0을 못가는 경우(시작도 못하는경우) false 리턴
    if 0 in [i[1] for i in order]:
        return False

    # a와 b는 선후 관계를 나타내는 딕셔너리. 시간복잡도 줄이기 위해.
    a = dict()
    b = dict()
    # d 는 나중에 큐에 넣을 노드 정보
    d = dict()
    for i in order:
        a[i[0]] = i[1]
        b[i[1]] = i[0]
    after = []

    visited = [False] * n
    graph = [[] for _ in range(n)]
    for i in range(len(path)):
        graph[path[i][0]].append(path[i][1])
        graph[path[i][1]].append(path[i][0])
    print(graph)

    q = deque([0]) #
    while q:
        node = q.popleft()
        visited[node] = True
        for tmp in graph[node]:
            if visited[tmp] is False and tmp not in b:
                q.append(tmp)
            elif visited[tmp] is False and tmp in b:
                node2 = b[tmp]
                if visited[node2] is True:
                    q.append(tmp)
                else:
                    d[tmp] = node2
            # 선행 노드가 처리된경우 after에서 처리가능한거 처리
        if node in a:
            node3 = a[node]
            if node3 in d and d[node3] != 'deleted':
                q.append(node3)
                d[node3] = 'deleted'
    print(visited)

    if False in visited:
        return False
    return True


print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))

# 효율성 실패.
# from collections import deque
#
# def solution(n, path, order):
#     # 0을 못가는 경우(시작도 못하는경우) false 리턴
#     if 0 in [i[1] for i in order]:
#         return False
#     answer = ""
#
#     a = dict()
#     b = dict()
#     for i in order:
#         a[i[0]] = i[1]
#         b[i[1]] = i[0]
#     after = []
#
#     visited = [False] * n
#     graph = [[] for _ in range(n)]
#     for i in range(len(path)):
#         graph[path[i][0]].append(path[i][1])
#         graph[path[i][1]].append(path[i][0])
#     print(graph)
#
#     q = deque([0]) #
#     while q:
#         node = q.popleft()
#         visited[node] = True
#         for tmp in graph[node]:
#             if visited[tmp] is False and tmp not in b:
#                 q.append(tmp)
#             elif visited[tmp] is False and tmp in b:
#                 node2 = b[tmp]
#                 if visited[node2] is True:
#                     q.append(tmp)
#                 else:
#                     after.append(tmp)
#             # 선행 노드가 처리된경우 after에서 처리가능한거 처리
#         if node in a:
#             node3 = a[node]
#             if node3 in after:
#                 q.append(node3)
#                 after.remove(node3)
#     print(visited)
#
#     if False in visited:
#         return False
#     return True
#
#
# print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))