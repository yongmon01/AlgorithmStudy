from itertools import combinations

n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

numbers = [10001] * 10000
numbers.insert(0, 0)

for i in coins:
    for j in range(len(numbers)-i):
        new_count = numbers[j] + 1
        numbers[j + i] = min(new_count, numbers[j + i])
if numbers[m] != 10001:
    print(numbers[m])
else:
    print(-1)







# possible_coins = [[3], [5], [7]]
# find = False
# c = 2
#
# # 이러면 무조건 시간초과..
# while not find:
#     new_possible_coins = []
#     for i in possible_coins:
#         last = i[-1]
#         index_last = coins.index(last)
#         for j in range(index_last, len(coins)):
#             new_current_coins = []
#             for k in i:
#                 new_current_coins.append(k)
#             new_current_coins.append(coins[j])
#             new_possible_coins.append(new_current_coins)
#     possible_coins = new_possible_coins
#     print(c, "..", possible_coins)
#     if sum(possible_coins[0]) > m:
#         print(-1)
#         break
#     for t in possible_coins:
#         if sum(t) == m:
#             print(c, 'answer = ', t)
#             find = True
#     c += 1




