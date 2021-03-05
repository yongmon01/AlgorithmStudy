# 숫자의 중복을 허용할때도 고려해보자

def b_search(li, start, end, target):
    if start > end:
        return -1
    middle = (start + end)//2
    if li[middle] == target:
        return middle
    elif li[middle] > target:
        return b_search(li, start, middle-1, target)
    else:
        return b_search(li, middle+1, end, target)

li = [1,1,2,2,2,2,3]
print(b_search(li, 0, len(li)-1, 3))


