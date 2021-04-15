# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 이거아님
# def union_parent(parent,a,b):
#     parent_a = find_parent(parent,a)
#     parent_b = find_parent(parent,b)
#     if parent_a < parent_b:
#         parent[b] = parent_a
#     else:
#         parent[a] = parent_b
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for i in range(m):
    p, q = map(int, input().split())
    union_parent(parent, p, q)

print(parent)
##
for i in parent:
    print(find_parent(parent, i), end=' ')

print(parent)
