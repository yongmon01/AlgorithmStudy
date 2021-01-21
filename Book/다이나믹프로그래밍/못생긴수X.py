# 무조건 시간초과
import time

n = int(input())
t1 = time.time()
def is_mot(num):
    if num == 1:
        return True
    while num % 2 == 0:
        num = num // 2
    while num % 3 == 0:
        num = num // 3
    while num % 5 == 0:
        num = num // 5
    if num == 1:
        return True
    else:
        return False

count = 0
num = 1
while count < n:
    if is_mot(num) is True:
        count += 1
        print(num)
    num += 1
# print(num-1)
t2 = time.time()
print(t2-t1)
