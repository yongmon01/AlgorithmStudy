n = int(input())
teams = list(map(int, input().split()))
# 등수가 바뀐 쌍의 수
m = int(input())
changed = []
for i in range(m):
    a, b = map(int, input().split())
    changed.append((a, b))
# print(n, teams, changed)


# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
#
# 3
# 2 3 1
# 0
#
# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3
