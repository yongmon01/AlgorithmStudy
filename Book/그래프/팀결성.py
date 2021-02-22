# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
# 총 n+1 명인겨
parent = [0] * (n + 1) # 부모 테이블 초기화하기
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n + 1):
    parent[i] = i

for i in range(m):
    exect, v1, v2 = map(int, input().split())
    if exect == 0:
        union_parent(parent, v1, v2)
    elif exect == 1:
        if find_parent(parent, v1) == find_parent(parent, v2):
            print('YES')
        else:
            print('NO')