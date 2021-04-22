# https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-python 참고
# 간단한데 생각을 못했다..
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    print(people)

    while people:
        if len(people) == 1:
            answer += 1
            break
        if people[0] + people[-1] > limit:
            people.pop()
            answer += 1
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1

    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))