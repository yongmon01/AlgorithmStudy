import heapq
food_times, k = [3, 1, 2], 5

if sum(food_times) <= k:
    print(-1)

q = []
for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i], i+1))
print(q)

prev, curr, total, length = 0, 0, 0, len(food_times)
while total + (q[0][0] - prev) * length <= k:
    curr = heapq.heappop(q)[0]
    total += (curr - prev) * length
    length -= 1
    prev = curr
q.sort(key = lambda x:x[1])
print(q[(k - total) % length][1])

# 땡
# for i in range(k):
#     if len(food_times) == 0:
#         print(-1)
#     index = i % len(food_times)
#     if food_times[index][1] == 1:
#         del food_times[index]
#     else:
#         food_times[index][1] -= 1
#     print(food_times)
#     if i + 1 == k:
#         print((i+1) % len(food_times)+1)


# 땡
# i = 0
# while food_times:
#     index = i % len(food_times)
#     if food_times[index][1] == 1:
#         del food_times[index]
#         i -= 1
#         k -= 1
#     else:
#         food_times[index][1] -= 1
#     print(food_times)
#     if i + 1 == k:
#         print(food_times[i % len(food_times)][0] + 1)
#         break
#     i += 1
























# 시간초과...

# def solution(food_times, k):
#     index, count = 0, 0
#     while count < k:
#         if food_times[index % len(food_times)] == 0:
#             index += 1
#             continue
#         food_times[index % len(food_times)] -= 1
#         index += 1
#         count += 1
#     for i in range(len(food_times)):
#         if food_times[(index) % len(food_times)] != 0:
#             return (index) % len(food_times) + 1
#         index += 1
#     return -1
