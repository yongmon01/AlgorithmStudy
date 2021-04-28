def merge_sort(my_list):

    if len(my_list) < 2:
        return my_list

    left = my_list[:len(my_list)//2]
    right = my_list[len(my_list)//2:]
    return merge(merge_sort(left), merge_sort(right))

def merge(list1, list2):
    return_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            return_list.append(list1[i])
            i += 1
        else:
            return_list.append(list2[j])
            j += 1
    if i < len(list1):
        return_list += list1[i:]
    if j < len(list2):
        return_list += list2[j:]
    return return_list

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))