# # 아 왜 이렇게 풀었을까... 문제 조건좀 잘 읽자...
# from itertools import permutations
#
# n = int(input())
# numbers = [i for i in range(1, n+1)]
# counts = list(map(int, input().split()))
# counts.insert(0,0)
#
# print(numbers, counts)
# candidates = list(permutations(numbers, n))
# print(candidates)
#
# for i in candidates:
#     find = True
#     for j in range(len(i)):
#         count = 0
#         for k in range(j, -1, -1):
#             if i[k] > i[j]:
#                 count += 1
#         if count != counts[i[j]]:
#             find = False
#             break
#     if find:
#         for a in i:
#             print(a, end=' ')



n = int(input())
counts = list(map(int, input().split()))
answer = [-1] * n
for i in range(len(counts)):
    c = 0
    print(answer)
    for j in range(len(counts)):
        if answer[j] != -1:
            continue
        if c == counts[i]:
            answer[j] = i + 1
        c += 1

for i in answer:
    print(i, end=' ')

