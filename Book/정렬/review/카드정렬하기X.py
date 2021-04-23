# 너무 단순히 생각했다.. 30 30 40 50 에서 30 와 30 을 더한 60 은 가장 크므로 맨뒤로 가야함..
# n = int(input()) 틀린 풀이 <- 무조건 리스트 앞에서 부터 계산하는 풀이.
# numbers = []
# for i in range(n):
#     numbers.append(int(input()))
# numbers.sort()
#
# answer, prev = 0, numbers[0]
# for i in range(n-1):
#     prev += numbers[i+1]
#     answer += prev
#
# print(answer)

import heapq
n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))

answer = 0
while len(q) > 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    answer += first + second
    heapq.heappush(q, first + second)

print(answer)
