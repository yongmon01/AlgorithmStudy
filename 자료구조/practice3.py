def merge_sort(a):

    if len(a) < 2:
        return

    i = 1
    while i < len(a):
        j = 0
        while j < len(a):
            print(i,j,j+i)
            merge(a, i, j)
            j += i+i
        i += i


def merge(my_list, i, j):

    left = my_list[j: j + i]
    right = my_list[j+i: j + i + i]
    l, r = 0, 0
    idx = j

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            my_list[idx] = left[l]
            l += 1
            idx += 1
        else:
            my_list[idx] = right[r]
            r += 1
            idx += 1

    while l < len(left):
        my_list[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        my_list[idx] = right[r]
        r += 1
        idx += 1

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
