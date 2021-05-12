def quick_sort(my_list, start, end):
    if start >= end:
        return

    part2 = partition(my_list, start, end)
    quick_sort(my_list, start, part2-1)
    quick_sort(my_list, part2, end)


def partition(my_list, start, end):
    i, j = start, end
    pivot = my_list[(start+end)//2]

    while i <= j:
        while my_list[i] < pivot:
            i += 1
        while my_list[j] > pivot:
            j -= 1
        if i <= j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
            j -= 1
    return i

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quick_sort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quick_sort(list2,0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quick_sort(list3, 0, len(list3) - 1)
print(list3)