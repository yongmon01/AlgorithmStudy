# 아 왜 이렇게 풀었을까...
from itertools import permutations
# 4
# 2 1 1 0

n = int(input())
numbers = [i for i in range(1, n+1)]
counts = list(map(int, input().split()))
counts.insert(0,0)

print(numbers, counts)
candidates = list(permutations(numbers, n))
print(candidates)

for i in candidates:
    find = True
    for j in range(len(i)):
        count = 0
        for k in range(j, -1, -1):
            if i[k] > i[j]:
                count += 1
        if count != counts[i[j]]:
            find = False
            break
    if find:
        for a in i:
            print(a, end=' ')
