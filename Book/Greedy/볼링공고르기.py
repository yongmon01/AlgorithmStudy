from itertools import combinations

n, m = map(int, input().split())
ball_list = list(map(int, input().split()))
answer = 0

possible_list = list(combinations(ball_list, 2))

for i in possible_list:
    if i[0] != i[1]:
        answer += 1

print(answer)