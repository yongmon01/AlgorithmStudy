# 아 이거 아니네... 반례) 10 20 30 40 50
# n = int(input())
#
# counts = []
# for i in range(n):
#     counts.append(int(input()))
# counts.sort()
#
# if n == 1:
#     print(0)
#
# else:
#     prev = counts[0]
#     total = 0
#     for i in range(1, len(counts)):
#         prev += counts[i]
#         total += prev
#     print(total)

# 이게 답..
import heapq
n = int(input())
counts = []
for i in range(n):
    heapq.heappush(counts, int(input()))

total = 0
while len(counts) != 1:
    one = heapq.heappop(counts)
    two = heapq.heappop(counts)
    sum = one + two
    total += sum
    heapq.heappush(counts, sum)
print(total)
