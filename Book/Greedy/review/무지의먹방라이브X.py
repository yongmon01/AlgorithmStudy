import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i],i))
    total, curr, prev, length = 0, 0, 0, len(food_times)
    while total + (q[0][0] - prev) * length <= k:
        curr = heapq.heappop(q)[0]
        total += (curr - prev) * length
        length -= 1
        print(total, 'total')
        prev = curr
    q.sort(key=lambda x: x[1])
    print(q[(k - total)// len(q)][1]+1)

solution([3,1,2],5)