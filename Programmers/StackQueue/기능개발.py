from collections import deque
def solution(progresses, speeds):
    answer = []
    dates = []
    for i in range(len(progresses)):
        j = 0
        while progresses[i] + j * speeds[i] < 100:
            j += 1
        dates.append(j)
    print(dates)
    
    dates = deque(dates)
    count = 1
    while dates:
        node = dates.popleft()
        while dates and dates[0] <= node:
            dates.popleft()
            count += 1
        answer.append(count)
        count = 1

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))