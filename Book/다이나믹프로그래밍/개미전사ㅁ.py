inputs = list(map(int, input().split()))

# 1 3 1 5
lists = [ [[1],1], [[],2] ]
del inputs[0]

for i in inputs:
    for j in range(len(lists)):
        print(lists)
        if lists[j][1] == 3:
            lists[j][0].append(i)
            lists[j][1] = 1
        elif lists[j][1] == 2:
            lists[j][1] = 3
            new_list = [[], 1]
            for k in lists[j][0]:
                new_list[0].append(k)
            new_list[0].append(i)
            lists.append(new_list)
            # print('new_list', new_list)
        elif lists[j][1] == 1:
            lists[j][1] = 2

answer_li = [sum(i[0]) for i in lists]
print(max(answer_li))

