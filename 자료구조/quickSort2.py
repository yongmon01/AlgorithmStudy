def quickSort(li, start, end):
    partition = pivot(li, start, end)
    if start < partition - 1:
        quickSort(li, start, partition - 1)
    if partition < end:
        quickSort(li, partition, end)

def pivot(li, start, end):

    middle = (start + end) // 2
    p = li[middle]

    while start <= end:
        while start < len(li) and li[start] < p:
            start += 1
        while end >= 0 and li[end] > p:
            end -= 1
        if end >= start:
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
    return start

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quickSort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quickSort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quickSort(list3, 0, len(list3) - 1)
print(list3)