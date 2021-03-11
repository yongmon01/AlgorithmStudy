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
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 이거틀림!!!
# def union_parent(parent, a, b):
#     p_a = find_parent(parent, a)
#     p_b = find_parent(parent, b)
#     if p_a < p_b:
#         parent[b] = p_a
#     else:
#         parent[a] = p_b
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

nodes = []

n, m = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    nodes.append((c,a,b))

nodes.sort()
answer = 0
parent = [i for i in range(n+1)]
print(parent)
print(nodes)

for node in nodes:
    cost, p, q = node
    if find_parent(parent, p) != find_parent(parent, q):
        answer += cost
        union_parent(parent, p, q)

print(answer)
print(parent)