from itertools import combinations

answer = int(1e9)
n, m = map(int, input().split())
graph = []
chickens = []
homes = []
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))
# print(graph)
# print(chickens)
# print('homes ',homes)

updated_chickens = list(combinations(chickens, m))
# print('updated_chickens ', updated_chickens)

for chicken in updated_chickens:
    current_answer = 0
    for i in homes:
        min_length = int(1e9)
        for j in chicken:
            min_length = min(min_length, abs(i[0] - j[0]) + abs(i[1] - j[1]))
        current_answer += min_length
    answer = min(answer, current_answer)

print(answer)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0