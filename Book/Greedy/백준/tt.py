# bisect 풀이
# nlog(n) 시간복잡도

import bisect

n = int(input())
numbers = list(map(int, input().split()))
dp = [-1] * n
answers = [numbers[0]]

for i in range(n):
    if numbers[i] > answers[-1]:
        answers.append(numbers[i])
        dp[i] = len(answers) - 1
    else:
        index = bisect.bisect_left(answers, numbers[i])
        answers[index] = numbers[i]
        dp[i] = index

return_list = []
count = max(dp)
for i in range(len(dp)-1, -1, -1):
    if dp[i] == count:
        return_list.append(numbers[i])
        count -= 1
return_list.sort()

print(len(return_list))
for i in return_list:
    print(i, end=' ')

print(return_list)
print(dp)
print(answers)