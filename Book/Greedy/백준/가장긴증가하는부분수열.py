# dp 풀이
# N ** 2 시간복잡도

n = int(input())
li = list(map(int, input().split()))

dp = [1] * (n)
for i in range(n):
    for j in range(i+1):
        if li[i] > li[j]:
            print(li[i], li[j])
            dp[i] = max(dp[i], dp[j]+1)

print(dp)