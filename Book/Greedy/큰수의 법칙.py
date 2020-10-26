# 94p

N, M, K = map(int, input().split())
array = input().split()
array = list(map(int, array))
array.sort(reverse=True)

count = 0
answer = 0

for i in range(M):
    if count < K:
        answer += array[0]
        count += 1
    else:
        answer += array[1]
        count = 0

print(answer)

# solution2

# b = M // (K+1)
# a = M - b
# answer2 = a * array[0] + b * array[1]
# print(answer2)



