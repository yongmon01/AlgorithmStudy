# bisect 풀이
# nlog(n) 시간복잡도

import bisect
n = int(input())
numbers = list(map(int, input().split()))
answer = [numbers[0]]
indexes = [-1] * (n)

for i in range(len(numbers)):
    if numbers[i] > answer[-1]:
        answer.append(numbers[i])
    else:
        index = bisect.bisect_left(answer, numbers[i])
        answer[index] = numbers[i]
    indexes[i] = answer.index(numbers[i])
print(indexes)
print(numbers)
# print(answer)
# max_count = max(indexes)
# ind = indexes.index(max_count)
# print(ind)
# for i in range(ind,-1,-1):
#     if indexes[i] == ind:
#         print(numbers[ind])
#     ind -= 1
answer_list = []
count = max(indexes)
for i in range(len(indexes)-1,-1,-1):
    if indexes[i] == count:
        answer_list.append(numbers[i])
        count -= 1
print(answer_list)

for i in answer_list[::-1]:
    print(i, end=' ')











# answer = list()
# answer.append(numbers[0])
# del numbers[0]
# # print(answer, numbers)
# real_answer = list()
# for i in answer:
#     real_answer.append(i)
#
# for i in numbers:
#     if i > answer[-1]:
#         answer.append(i)
#     else:
#         index = bisect.bisect_left(answer, i)
#         answer[index] = i
#     if real_answer[-1] != answer[-1]:
#         real_answer.clear()
#         for j in answer:
#             real_answer.append(j)
#
# print(len(real_answer))
# for i in real_answer:
#     print(i, end=' ')

# 6
# 10 20 10 30 20 50

# 10
# 10 20 10 30 25 20 50 25 30 40

# 11
# 10 20 10 30 25 20 50 25 30 40 27