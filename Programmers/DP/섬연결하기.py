# 크루스칼 알고리즘 이용하여 무난히 풀었다.
import heapq


def solution(n, costs):
    answer = 0

    parent = [i for i in range(n)]
    q = []
    for i in costs:
        heapq.heappush(q, (i[2], i[0], i[1]))
    while q:
        l, a, b = heapq.heappop(q)
        if find_parent(parent, a) != find_parent(parent, b):
            answer += l
            union_parent(parent, a, b)

    return answer


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a
    elif b < a:
        parent[a] = b