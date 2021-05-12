def merge_sort(li):
    if len(li) < 2:
        return
    left = li[:len(li)//2]
    right = li[len(li)//2:]

    merge_sort(left)
    merge_sort(right)

    merge(li,left,right)

def merge(whole, left, right):
    i, j = 0, 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            whole[k] = left[i]
            k += 1
            i += 1
        else:
            whole[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        whole[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        whole[k] = right[j]
        k += 1
        j += 1
    return


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)

d1 = [1, 3, 5, 7, 9, 11, 13, 11]
d2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
d3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
merge_sort(d1)
merge_sort(d2)
merge_sort(d3)
print(d1)
print(d2)
print(d3)