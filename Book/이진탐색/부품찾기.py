import sys

def b_search(li, start, end, target):
    if start > end:
        return 'no'
    middle = (start + end)//2
    if li[middle] == target:
        return 'yes'
    elif li[middle] > target:
        return b_search(li, start, middle-1, target)
    else:
        return b_search(li, middle+1, end, target)

n = int(input())
have = list(map(int, sys.stdin.readline().rstrip().split()))
have.sort()
m = int(input())
need = list(map(int, sys.stdin.readline().rstrip().split()))

for i in need:
    print(b_search(have, 0, len(have)-1, i), end=' ')