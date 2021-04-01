# import bisect
# # li = [1, 3, 5, 7, 9]
# # idx = bisect.bisect_left(li, 2)
# # print(idx)
# #
# # li2 = [1,2,3,4,5]
# # print(li2[::-1])

# def solution(n):
#     answer = 1
#     for i in range(1,n+1):
#         answer *= i
#     answer = str(answer)
#     count = 0
#     for i in answer[::-1]:
#         if i == '0':
#             count += 1
#         else:
#             break
#     print(n)
#     print(answer)
#     return count

# for i in range(1,21):
#     print(solution(i))


# print(solution(10000))
#
# def solution(n):
#     answer = 1
#     for i in range(1,n+1):
#         answer *= i
#     answer = str(answer)
#     count = 0
#     for i in answer[::-1]:
#         if i == '0':
#             count += 1
#         else:
#             break
#     return count
#
# def solution(n):
#     count_two = 0
#     count_five = 0
#
#     for i in range(1, n+1):
#
#         while i % 2 == 0:
#             count_two += 1
#             i //= 2
#
#         while i % 5 == 0:
#             count_five += 1
#             i //= 5
#
#     return min(count_two, count_five)
# print(count_zero(10))

def count_trailing_zeros(N):
    # 1.
    cache = [-1] * (N+1)

    def count_factors(n, f):
        # 2.
        if cache[n] != -1:
            return cache[n]

        # 3.
        cache[n] = count_factors(n // f, f) + 1 if not n % f else 0
        return cache[n]

    # 4.
    ans = 0
    for i in range(1, N+1):
        ans += count_factors(i, 5)
    return ans

# print(count_trailing_zeros(1000000))

li = [1,5,2]
