li = [3,5,2,6,1,9,4,8]

def mSort(li):
    if len(li) < 2:
        return li
    else:
        middle = len(li) // 2
        print(middle)
        left = li[:middle]
        right = li[middle:]
        print(left, right)

        # mSort(left)
        # mSort(right)

        return merge(mSort(left), mSort(right)) #

def merge(list1, list2):
    answer = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            answer.append(list1[i])
            i += 1
        else:
            answer.append(list2[j])
            j += 1
    if i == len(list1):
        while j < len(list2):
            answer.append(list2[j])
            j += 1
    else:
        while i < len(list1):
            answer.append(list1[i])
            i += 1
    return answer


print(mSort(li))
print(li)
