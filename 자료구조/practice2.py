def merge(my_list, left, right):

    i = 0
    j = 0
    l = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            my_list[l] = right[j]
            j += 1
            l += 1
        else:
            my_list[l] = left[i]
            i += 1
            l += 1

    while i < len(left):
        my_list[l] = left[i]
        i += 1
        l += 1
    while j < len(right):
        my_list[l] = right[j]
        j += 1
        l += 1


def merge_sort(my_list):

    if len(my_list) < 2:
        return my_list

    left = my_list[:len(my_list)//2]
    right = my_list[len(my_list)//2:]
    merge_sort(left)
    merge_sort(right)

    merge(my_list, left, right)

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