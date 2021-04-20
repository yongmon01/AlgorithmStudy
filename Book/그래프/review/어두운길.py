import heapq
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
total, answer = 0, 0

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif b < a:
        parent[a] = b

q  = []
for i in range(m):
    x, y, z = map(int, input().split())
    total += z
    heapq.heappush(q, (z, x, y))

while q:
    z, x, y = heapq.heappop(q)
    if find_parent(parent, y) != find_parent(parent, x):
        union_parent(parent, x, y)
        answer += z

print(total - answer)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11