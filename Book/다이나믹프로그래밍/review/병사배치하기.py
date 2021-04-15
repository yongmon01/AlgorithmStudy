# 7
# 15 11 4 8 5 2 4

n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if numbers[i] < numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(n - max(dp) - 1)