from bisect import bisect_left
def solution(citations):
    citations.sort()
    h = len(citations)
    while h > 0:
        index = bisect_left(citations, h)
        if len(citations) - index >= h and index <= h:
            break
        h -= 1
    return h

citations = [3, 0, 6, 1, 5]
print(solution(citations))