n = int(input())
scary = list(map(int, input().split()))
scary.sort()

answer = 0

count = 1
for i in range(len(scary)):
    # print(scary[i], count, answer)
    if scary[i] <= count:
        answer += 1
        count = 1
    else:
        count += 1

print(answer)



# 20
# 1 1 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 6 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 10

# 5
# 2 3 1 2 2