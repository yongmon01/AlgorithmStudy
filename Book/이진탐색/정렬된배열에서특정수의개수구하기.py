import sys
n, x = map(int, input().split())
input_data = sys.stdin.readline().rstrip()
input_data = list(map(int, input_data.split()))

def b_search(li, start, end, target):
    if start > end:
        return -1
    middle = (start + end)//2
    if li[middle] == target:
        return middle
    elif li[middle] > target:
        return b_search(li, start, middle-1, target)
    else:
        return b_search(li, middle+1, end, target)

index = b_search(input_data, 0, len(input_data)-1, x)

if index == -1:
    print(0)
else:
    count = 0
    index_1 = index
    index_2 = index + 1
    while index_1 >= 0 and input_data[index_1] == x:
        count += 1
        index_1 -= 1
    while index_2 <= len(input_data)-1 and input_data[index_2] == x:
        count += 1
        index_2 += 1
    print(count)