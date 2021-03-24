# bisect 풀이
# nlog(n) 시간복잡도

import bisect
n = int(input())
li = list(map(int, input().split()))

dp = [li[0]]
for i in li:
    if i > dp[-1]:
        dp.append(i)
    else:
        idx = bisect.bisect_left(dp, i)
        dp[idx] = i
print(len(dp))
print(dp)