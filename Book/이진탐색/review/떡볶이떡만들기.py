n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

print(n, m)
print(li)

def b_search(start, end, m):
    middle = (start+end)//2
    if start > end:
        return -1
    elif success(middle) and not success(middle + 1):
        return middle
    elif success(middle):
        return b_search(middle+1, end, m)
    else:
        return b_search(start, middle-1, m)

def success(length):
    result = 0
    for i in li:
        if i > length:
            result += i - length
    if result >= m:
        return True
    return False

print(b_search(li[0],li[n-1],m))



# 4 6
# 19 15 10 17