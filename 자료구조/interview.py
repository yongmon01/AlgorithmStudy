# Merge
# 함수
# 를
# 구현하십시오.
#
# 예)
# a = [1, 3, 6, 7, 9]  # 정렬되어 있음.
# b = [2, 5, 8, 10, 11, 12]  # 정렬되어 있음.
#
# result = merge(a, b)
#
# result = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]  # 정렬되어 있음.
#
#          - -----------------------------------------------------------------------------------------------------------------
#
# Def
# merge(a, b):
#
# Return_list = []
#
# I, j = 0, 0
# While
# i < len(a) and j < len(b):
# If
# a[i] <= b[j]:
# return_list.append(a[i])
# I += 1
# Else:
# return_list.append(b[j])
# J += 1
#
# If
# i < len(a):
# Return_list += a[i:]
# If
# j < len(b):
# Return_list += b[j:]
#
# Return
# return_list
#
# Merge
# sort
# 구현
# 하세요.
#
#     Def
# merge_sort(my_list):
#
# If
# len(my_list) < 2:
# Return
# my_list
#
# Left = my_list[:len(my_list) // 2]
# Right = my_list[len(my_list) // 2:]
#
# Left = merge_sort(left)
# Right = merge_sort(right)
#
# Return
# merge(left, right)
#
