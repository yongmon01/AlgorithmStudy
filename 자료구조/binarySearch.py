def binary_search(my_list, start, end, target):
    if end < start:
        return -1

    middle = (start + end) // 2
    if my_list[middle] == target:
        return middle
    elif my_list[middle] > target:
        return binary_search(my_list, start, middle-1, target)
    else:
        return binary_search(my_list, middle+1, end, target)

li1 = [1, 3, 5, 7, 9, 11, 11, 13]
print(binary_search(li1, 0, len(li1)-1, 1))
li2 = [1, 5, 7, 9, 13, 15, 28, 30, 48]
li3 = [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]