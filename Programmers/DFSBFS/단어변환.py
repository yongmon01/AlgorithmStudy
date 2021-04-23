# bfs 가 숫자가아닌 문자열인 문제. 무난히 풀수있었다.
from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    words.insert(0, begin)

    visited = [False] * (len(words) + 1)
    distance = [0] * (len(words) + 1)
    q = deque()
    q.append(begin)
    visited[0] = True

    while q:
        node = q.popleft()
        print(node)
        for w in words:
            if check(node, w) is True and visited[words.index(w)] is False:
                distance[words.index(w)] = distance[words.index(node)] + 1
                q.append(w)
                visited[words.index(w)] = True

    return distance[words.index(target)]


def check(first, second):
    count = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            count += 1
    if count == len(first) - 1:
        return True
    else:
        return False

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
