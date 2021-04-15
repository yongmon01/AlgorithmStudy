n = int(input())

dp = [False] * 2002
dp[1] = True

for i in range(1, 1001):
    if dp[i] is True:
        if 2 * i < 2002:
            dp[2*i] = True
for i in range(1, 1001):
    if dp[i] is True:
        if 3 * i < 2002:
            dp[3*i] = True
for i in range(1, 1001):
    if dp[i] is True:
        if 5 * i < 2002:
            dp[5*i] = True
# print(dp[:20])

i = 1
while n > 0:
    if dp[i] is True:
        n -= 1
    i += 1
print(i - 1)