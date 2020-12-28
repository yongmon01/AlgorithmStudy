from itertools import combinations
n, m = map(int, input().split())
town = []
for i in range(n):
    town.append(list(map(int, input().split())))

homes = []
chickens = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            homes.append((i, j))
        if town[i][j] == 2:
            chickens.append((i, j))

print('homes', homes)
#print(chickens)
chicken_lengths = []

for i in range(1, m+1):
    # i 개 고르기
    current_chickens_list = list(combinations(chickens, i))
    print('current_chickens_list', current_chickens_list)
    for current_chickens in current_chickens_list:
        current_length = 0
        for home in homes:
            lengt = []
            for chicken in current_chickens:
                lengt.append(abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
            current_length += min(lengt)
        chicken_lengths.append(current_length)

print(chicken_lengths)
print(min(chicken_lengths))

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2