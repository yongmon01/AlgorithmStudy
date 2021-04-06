# import bisect
#
# n, x = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# left = bisect.bisect_left(numbers, x)
# right = bisect.bisect_right(numbers, x)
#
# if left == right:
#     print(-1)
# else:
#     print(right - left)

n, x = map(int, input().split())
numbers = list(map(int, input().split()))

def bsearch(start, end, target):
    if end < start:
        return -1

    middle = (start + end) // 2
    if numbers[middle] == target:
        return middle
    elif numbers[middle] > target:
        return bsearch(start, middle-1, target)
    else:
        return bsearch(middle + 1, end, target)

print(bsearch(0, 7, 8))

# 7 2
# 1 1 2 2 2 2 4
