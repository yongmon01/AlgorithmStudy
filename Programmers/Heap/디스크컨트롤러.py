# 나의 heapq풀이

import heapq
def solution(jobs):
    current_time, temp, times, n = 0, [], [], len(jobs)
    answer = 0
    for i in range(len(jobs)):
        jobs[i][0], jobs[i][1] = jobs[i][1], jobs[i][0]
    heapq.heapify(jobs)
    while jobs:
        min_t = min(list(i[1] for i in jobs))
        if min_t > current_time:
            current_time = min_t
            continue
        disk = heapq.heappop(jobs)
        while disk[1] > current_time:
            temp.append(disk)
            disk = heapq.heappop(jobs)
        for d in temp:
            heapq.heappush(jobs, d)
        temp.clear()

        current_time += disk[0]
        times.append(current_time - disk[1])

    return sum(times) // n

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))










# import heapq
# def solution(jobs):
#     answer = 0
#     # jobs_sort_by_time =
#     jobs.sort()
#     times = []
#     current_time = jobs[0][0] + jobs[0][1]
#     times.append(current_time - jobs[0][0])
#     del jobs[0]
#     for i in range(len(jobs)):
#         jobs[i][0], jobs[i][1] = jobs[i][1], jobs[i][0]
#     heapq.heapify(jobs)
#     # print(jobs)
#     count = 0
#     while jobs:
#         disk = heapq.heappop(jobs)
#         if disk[1] > current_time:
#             count += 1
#
#
#     return answer
#
# jobs = [[0, 3], [1, 9], [2, 6]]
# print(solution(jobs))