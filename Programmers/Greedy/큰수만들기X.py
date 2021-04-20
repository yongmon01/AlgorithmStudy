from collections import deque
def solution(number, k):
    answer = deque()
    for i in number:
        if not answer:
            answer.append(i)
            continue
        elif k == 0:
            answer.append(i)
            continue
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    for i in range(k):
        answer.pop()

    return "".join(list(answer))
print(solution("1231234",3))