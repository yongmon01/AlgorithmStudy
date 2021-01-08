import sys
# n = int(input())
# input_data = list(map(int, sys.stdin.readline().rstrip().split()))
# print(input_data)

def p_search(li, start, end):
    if start > end:
        return -1
    middle = (start + end)//2
    if li[middle] == middle:
        return middle
    elif li[middle] > middle:
        return p_search(li, start, middle-1)
    else:
        return p_search(li, middle+1, end)

li = [-15,-4,2,8,9,13,15]
print(p_search(li,0,6))
li2 = [-15,-6,1,3,7]
print(p_search(li2,0,6))