def merge_sort(my_list):

    if len(my_list) < 2:
        return my_list

    left = my_list[:len(my_list)//2]
    right = my_list[len(my_list)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):

    return_list = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            return_list.append(left[i])
            i += 1
        else:
            return_list.append(right[j])
            j += 1

    if i < len(left):
        return_list += left[i:]
    if j < len(right):
        return_list += right[j:]

    return return_list

#
#
#
#
#
#
#
#
# # def merge_sort(my_list):
# #
# #     if len(my_list) < 2:
# #         return my_list
# #
# #     left = merge_sort(my_list[:len(my_list)//2])
# #     right = merge_sort(my_list[len(my_list)//2:])
# #
# #     return merge(left, right)
# #
# # def merge(left, right):
# #
# #     return_list = []
# #     i, j = 0, 0
# #     while i < len(left) and j < len(right):
# #         if left[i] <= right[j]:
# #             return_list.append(left[i])
# #             i += 1
# #         else:
# #             return_list.append(right[j])
# #             j += 1
# #
# #     if i < len(left):
# #         return_list += left[i:]
# #     if j < len(right):
# #         return_list += right[j:]
# #
# #     return return_list
# def merge_sort(my_list):
#     if len(my_list) < 2:
#         return my_list
#
#     left = merge_sort(my_list[:len(my_list) // 2])
#     right = merge_sort(my_list[len(my_list) // 2:])
#
#     return merge(left, right)
#
#
# def merge(left, right):
#     return_list = []
#
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             return_list.append(left[i])
#             i += 1
#         else:
#             return_list.append(right[j])
#             j += 1
#
#     if i < len(left):
#         return_list += left[i:]
#     if j < len(right):
#         return_list += right[j:]
#
#     return return_list

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))