from bisect import bisect_left

def b_left(a, x, lo=0, hi=None):
  if lo < 0:
    raise ValueError('lo must be non-negative')
  if hi is None:
    hi = len(a)
  while lo < hi:
    mid = (lo + hi) // 2  ## 찾는 범위의 중간위치를 구해서
    if a[mid] < x : lo = mid + 1  ## 찾는 값이 더 크면 오른쪽 절반으로 범위 축소
    else: hi = mid  ## 크거나 같으면 왼쪽 절반으로 범위 축소.
    ## 이 때, lo == hi 가 되면 찾은 것이고, lo > hi 가 되면 없는 것이다.
  return lo

li = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(b_left(li,0,0,len(li)-1))
print(bisect_left(li, 20))

# result = 0
# l, r = 0, len(li)-1
# while l <= r:
#   mid = (l+r) // 2
#   if li[mid] >= 20:
#     result = mid
#     r = mid - 1
#   else: l = mid + 1
# print(result)


def bisect_l(arr, value, begin, end):
  if begin >= end:
    return begin
  mid = begin + (end - begin) // 2
  if arr[mid] < value:
    return bisect_left(arr, value, mid + 1, end)
  else:
    return bisect_left(arr, value, begin, mid)

print(bisect_l(li,20,0,len(li)-1))


# from bisect import bisect_left
#
# def b_l(li, target, low, hi):
#     while low < hi:
#         middle = (low + hi) // 2
#         if li[middle] >= target:
#             hi = middle
#             print('hi', hi)
#         elif li[middle] < target:
#             low = middle + 1
#             print('low', low)
#     return low
#
# li = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(b_l(li,20,0,len(li)-1))
# print(bisect_left(li, 20))


