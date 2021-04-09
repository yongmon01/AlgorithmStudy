import heapq

answer = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
q = []
parent = [i for i in range(n+1)]
print(parent)

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

for _ in range(m):
    c, a, b = heapq.heappop(q)
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        answer += c
        union_parent(parent, a, b)

print(answer)



# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25