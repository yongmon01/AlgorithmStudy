from bisect import bisect_left, bisect_right
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def count_num(li, a, b):
    num1 = bisect_right(li, b)
    num2 = bisect_left(li, a)
    return num1 - num2

words_li = [[] for _ in range(10)]
reversed_words_li = [[] for _ in range(10)]
for w in words:
    words_li[len(w)].append(w)
    reversed_words_li[len(w)].append(w[::-1])
for i in range(len(words_li)):
    words_li[i].sort()
    reversed_words_li[i].sort()

print(words_li)
print(reversed_words_li)

answer = []
for q in queries:
    if q.startswith("?"):
        answer.append(count_num(reversed_words_li[len(q[::-1])],q[::-1].replace('?','a'),q[::-1].replace('?','z')))
    elif q.endswith("?"):
        answer.append(count_num(words_li[len(q)], q.replace('?', 'a'), q.replace('?', 'z')))
print(answer)
# 에러!!!!
# import re
#
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao", "dnf"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?nf", "?????"]
#
# reverse_words = [w[::-1] for w in words]
# reverse_queries = [q[::-1] for q in queries]
#
# words.sort()
# reverse_words.sort()
# print('words, ', words)
# print('queries', queries)
# print('reverse_words: ', reverse_words)
# print('reverse_queries', reverse_queries)
#
# def b_search(li, start, end, target, length):
#     if start >= end:
#         return 0
#     middle = (start + end)//2
#     if li[middle].startswith(target):
#         if len(li[middle]) == length:
#             count = 1
#         else:
#             count = 0
#         s, e = middle-1, middle+1
#         # c_li = [li[middle]]
#         while li[s].startswith(target):
#             if len(li[s]) == length:
#                 count += 1
#             # c_li.append(li[s])
#             s -= 1
#         while li[e].startswith(target):
#             if len(li[e]) == length:
#                 count += 1
#             # c_li.append(li[e])
#             e += 1
#         # print(c_li)
#         return count
#     elif li[middle] > target:
#         return b_search(li, start, middle, target, length)
#     else:
#         return b_search(li, middle+1, end, target, length)
#
# result = []
#
# for i in range(len(queries)):
#     print(queries[i])
#     length = len(queries[i])
#     if queries[i].endswith("?") and queries[i].startswith("?"):
#         count = 0
#         for w in words:
#             if len(w) == length:
#                 count += 1
#         result.append(count)
#     elif queries[i].endswith("?"):
#         new_word = queries[i].replace("?", "")
#         result.append(b_search(words, 0, len(words)-1, new_word, length))
#     elif queries[i].startswith("?"):
#         new_word = reverse_queries[i].replace("?", "")
#         result.append(b_search(reverse_words, 0, len(reverse_words) - 1, new_word, length))
#
# print(result)
