# 맞지만 시간초과.. 일부는 통과..
from collections import deque
def solution(people, limit):
    answer = 0

    people.sort()
    people = deque(people)
    while people:
        w = people.popleft()
        answer += 1
        i = 0
        while i < len(people) and w + people[i] <= limit:
            i += 1
        if i == 0:
            continue
        else:
            people.remove(people[i-1])

    return answer

people = [20,30,40,50,50,70,80]
limit = 100
print(solution(people,limit))
