# 멍청하게 풀었다..
# hour = 0
# min = 0
# sec = 0
# count = 0
#
# n = int(input())
#
# while hour != n or min != 59 or sec != 59:
#     if '3' in str(hour) or '3' in str(min) or '3' in str(sec):
#         count += 1
#     sec += 1
#     if sec >= 60:
#         sec = 0
#         min += 1
#     if min >= 60:
#         hour += 1
#         min = 0
#     # print(hour,min,sec)
#
# print(count)

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)