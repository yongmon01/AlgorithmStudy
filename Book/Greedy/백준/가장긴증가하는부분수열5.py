# bisect 풀이
# nlog(n) 시간복잡도

import bisect
n = int(input())
li = list(map(int, input().split()))
graph = [[] for _ in range(n)]
answer = [li[0]]

dp = [li[0]]
for i in li:
    if i > dp[-1]:
        dp.append(i)
        answer.append(i) #

    else:
        idx = bisect.bisect_left(dp, i)
        dp[idx] = i
        idx2 = bisect.bisect_left(answer, i) #
        answer[idx2] = i #
print(len(dp))
print(dp)
print(answer)