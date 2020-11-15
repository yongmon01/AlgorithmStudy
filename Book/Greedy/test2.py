import heapq

h = []
heapq.heappush(h, (-5, 'write code'))
heapq.heappush(h, (-7, 'release product'))
heapq.heappush(h, (-1, 'write spec'))
heapq.heappush(h, (-3, 'create tests'))

result = []


while h:
    value = heapq.heappop(h)
    result.append((-value[0], value[1]))

print(result)
