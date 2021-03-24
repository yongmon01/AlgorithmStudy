import bisect
li = [1, 3, 5, 7, 9]
idx = bisect.bisect_left(li, 2)
print(idx)