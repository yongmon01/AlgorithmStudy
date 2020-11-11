# 1 2 2 2 3
# 1 2 3 4

n = int(input())
people = list(map(int, input().split()))
people.sort()

answer = 0
count = 0

for i in people:
    count += 1
    if count >= i:
        answer += 1
        count = 0


print(answer)