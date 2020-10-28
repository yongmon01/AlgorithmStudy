N, M = map(int, input().split())

min_list = []

for i in range(N):
    row = list(map(int, input().split()))
    minimum = min(row)
    min_list.append(minimum)

print(max(min_list))

