from bisect import bisect_left
from copy import deepcopy
target_num = input()
target = [int(i) for i in target_num]
n = int(input())
broken = list(map(int, input().split()))
numbers = [i for i in range(10)]
for i in broken:
    numbers.remove(i)
# numbers.append(0)
# numbers.insert(0, 9)

if len(numbers) == 0:
    print(abs(100-int(target_num)))
    quit()

print(numbers)
print(target)
near_target = []
for i in target:
    if i in numbers:
        # index = numbers.index(i)
        near_target.append(i)
    else:
        right = bisect_left(numbers, i)
        left = right - 1
        if right >= len(numbers):
            right = 0
        print(left, right)
        near_target.append((numbers[left], numbers[right]))
print('near_target ',near_target)

candidates = []
if type(near_target[0]) != tuple:
    candidates.append(str(near_target[0]))
else:
    candidates.append(str(near_target[0][0]))
    candidates.append(str(near_target[0][1]))
del near_target[0]

for i in range(len(near_target)):
    if type(near_target[i]) != tuple:
        for j in range(len(candidates)):
            candidates[j] += str(near_target[i])
    else:
        new_li = []
        for j in range(len(candidates)):
            new1 = candidates[j] + str(near_target[i][0])
            new2 = candidates[j] + str(near_target[i][1])
            new_li.append(new1)
            new_li.append(new2)
        candidates = deepcopy(new_li)

count = []
nogada = abs(100-int(target_num))
for i in candidates:
    count.append(abs(int(i)-int(target_num)))
if min(count) > nogada:
    print(nogada)
else:
    print(min(count) + len(target_num))


print('near_target ', near_target)
print(candidates)


# 5457
# 3
# 6 7 8


# from bisect import bisect_left
# from copy import deepcopy
# target = list(map(int, input()))
# n = int(input())
# broken = list(map(int, input().split()))
# numbers = [i for i in range(10)]
# for i in broken:
#     numbers.remove(i)
# # numbers.append(0)
# # numbers.insert(0, 9)
# print(numbers)
# print(target)
# near_target = []
# for i in target:
#     if i in numbers:
#         # index = numbers.index(i)
#         near_target.append(i)
#     else:
#         right = bisect_left(numbers, i)
#         left = right - 1
#         if right > len(numbers):
#             right = 0
#         near_target.append((numbers[left], numbers[right]))
# print('near_target ',near_target)
#
# candidates = []
# if type(near_target[0]) != tuple:
#     candidates.append(near_target[0])
# else:
#     candidates.append(near_target[0][0])
#     candidates.append(near_target[0][1])
# del near_target[0]
#
# for i in range(len(near_target)):
#     if type(near_target[i]) != tuple:
#         for j in range(len(candidates)):
#             candidates[j] += near_target[i]
#     else:
#         new_li = []
#         for j in range(len(candidates)):
#             new1 = candidates[j] + near_target[i][0]
#             new2 = candidates[j] + near_target[i][1]
#             new_li.append(new1)
#             new_li.append(new2)
#         candidates = deepcopy(new_li)
#
#
#
# print('near_target ', near_target)
# print(candidates)
#
#
# # 5457
# # 3
# # 6 7 8