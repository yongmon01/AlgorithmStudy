li = [3,5,2,6,1,9,4,8]

middle = len(li) // 2
p = li[middle]
i, j = 0, len(li) - 1

def quickSort(li, start=0, end=len(li)-1):
    partition = pivot(li, start, end)
    if start < partition - 1:
        quickSort(li, start, partition - 1)
    if partition < end:
        quickSort(li, partition, end)

def pivot(li, start, end):
    middle = (start + end) // 2
    print('li',li)
    print('middle',middle)
    p = li[middle]

    while start <= end:
        while start < len(li) and li[start] < p:
            start += 1
        while end >= 0 and li[end] > p:
            end -= 1
        print(start, end)
        if end >= start:
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
    return start

quickSort(li)
print(li)