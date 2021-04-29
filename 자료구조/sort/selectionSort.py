# 불안정 정렬 / 시간 O(n**2) / 공간 O(n)
def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[min_index], my_list[i] = my_list[i], my_list[min_index]


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
selection_sort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
selection_sort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
selection_sort(list3)
print(list3)
