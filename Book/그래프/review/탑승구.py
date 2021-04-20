g = int(input())
p = int(input())
count = 0
plains = [-1]
for i in range(p):
    plains.append(int(input()))
visited = [i for i in range(g+1)]

print(plains)
print(visited)

for i in range(1, g+1):
    print(i)
    num = plains[i]
    max_num = max(visited[:num+1])
    if max_num == 0:
        break
    visited[max_num] = 0
    count += 1
    print(visited)

print(count)

# count = 0
# max_p = 0
# last = 0
#
# for i in plains:
#     if i <= last:
#         break
#     count += 1
#     max_p = max(max_p, i)
#     if count == max_p:
#         last = max_p
#
# print(count)

# 4
# 3
# 4
# 1
# 1