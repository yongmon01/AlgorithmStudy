from itertools import combinations
min_answer = 10000

string = "aaaabbbbc"
string_list = list(string)
print(string_list)

n = 5
for i in range(n):
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print('********',i)
    com = combinations(string_list, i)
    print(list(com))
    for j in com:
        dic[j] -= 1
    max_num = max(list(map(int,dic.values())))
    min_num = min(list(map(int,dic.values())))
    min_answer = min(min_answer, max_num - min_num)
print(min_answer)







# page = 5457
# broken = [6, 7, 8]
#
# enable_set = {str(i) for i in range(10)}
# broken_set = set(list(map(str, broken)))
# enable_set = enable_set - broken_set
# for i in range(10):
#     if i not in broken:
#         enable_set.add(str(i))
#
# count = abs(100 - page)
#
# for n in range(1000001):
#     n = str(n)
#     for j in range(len(n)):
#         if n[j] not in enable_set:
#             break
#         elif j == len(n) - 1:
#             count = min(count, abs(page - int(n)) + len(str(n)))
#
# print(count)