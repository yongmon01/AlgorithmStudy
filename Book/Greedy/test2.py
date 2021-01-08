from bisect import bisect_left, bisect_right

li = [1,2,3,4,4,5,6,7,8]
print(bisect_left(li,4))
print(bisect_right(li,4))