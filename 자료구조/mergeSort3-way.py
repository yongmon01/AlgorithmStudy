# 머지소트 top down 하향식 return 있는 식.

def merge(list1, list2, list3):
    i = 0
    j = 0
    k = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2) and k < len(list3):
        min_num = min(list1[i], list2[j], list3[k])
        merged_list.append(min_num)
        if min_num == list1[i]:
            i += 1
        elif min_num == list2[j]:
            j += 1
        elif min_num == list3[k]:
            k += 1

    # list3 가 비었을때
    if i < len(list1) and j < len(list2):
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        if i < len(list1):
            merged_list += list1[i:]
        if j < len(list2):
            merged_list += list2[j:]

    # list2 가 비었을때
    if i < len(list1) and k < len(list3):
        while i < len(list1) and k < len(list3):
            if list1[i] <= list3[k]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list3[k])
                k += 1
        if i < len(list1):
            merged_list += list1[i:]
        if k < len(list3):
            merged_list += list3[k:]

    # list1 가 비었을때
    if k < len(list3) and j < len(list2):
        while k < len(list3) and j < len(list2):
            if list3[k] <= list2[j]:
                merged_list.append(list3[k])
                k += 1
            else:
                merged_list.append(list2[j])
                j += 1
        if k < len(list3):
            merged_list += list3[k:]
        if j < len(list2):
            merged_list += list2[j:]


    return merged_list


def merge_sort(my_list):
    # base case
    if len(my_list) < 3:
        return sorted(my_list)

    # my_list를 세개로 나눈다(divide)
    left = my_list[:len(my_list)//3]    # 왼쪽 반
    middle = my_list[len(my_list)//3: len(my_list)//3*2]   # 오른쪽 반
    right = my_list[len(my_list)//3*2:]

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    return merge(merge_sort(left), merge_sort(middle), merge_sort(right))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))