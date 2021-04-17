# heapq를 안쓰고 푼 풀이

def solution(jobs):
    n = len(jobs)
    answer = 0
    times = []
    jobs.sort()
    current_time = 0
    while jobs:

        # 현재 처리할수있는 디스크가 없을때
        if jobs[0][0] > current_time:
            current_time = jobs[0][0]
            continue

        # 처리할수있는 디스크가 있을때
        min_take_time = int(1e9)
        min_index = -1
        i = 0
        while i < len(jobs) and jobs[i][0] <= current_time:
            if min_take_time > jobs[i][1]:
                min_take_time = jobs[i][1]
                min_index = i
            i += 1
        times.append(current_time + min_take_time - jobs[min_index][0])
        current_time += min_take_time
        del jobs[min_index]

    return sum(times) // n

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
