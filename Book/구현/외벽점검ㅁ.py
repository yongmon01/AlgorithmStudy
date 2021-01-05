from itertools import permutations

# n = 12
# weak_list = [1,5,6,10]
# dist = [4,3,2,1] ###################
n = 12
weak_list_origin = [1,3,4,9,10]
dist = [3,5,7]
# dist = [1,1]

###############################################################
per_dist = list(permutations(dist, len(dist)))
print(per_dist)
count_list = []
##
is_okay = False
weak, weaks = [], []
for i in weak_list_origin:
    weak.append(i)
weaks.append(weak)
for k in range(len(weak) - 1):
    new_list = []
    prev_list = weaks[-1]
    first = prev_list[0]
    for q in range(1, len(prev_list)):
        new_list.append(prev_list[q])
    new_list.append(n + first)
    weaks.append(new_list)
print(weaks)

for weak_list in weaks:
    for d in per_dist:
        count = 0
        weak = []
        for i in weak_list:
            weak.append(i)

        print(weak_list)
        print(d)
        for i in range(len(d)):
            if len(weak) == 0:
                break
            curr_length = d[i]
            from_length = weak[0] + curr_length
            while weak and weak[0] <= from_length:
                del weak[0]
            count += 1

        if len(weak) == 0:
            is_okay = True
        print(is_okay)

        count_list.append(count)
        print("count - ", count)
if is_okay == False:
    print('nono')
else:
    print(count_list)

###########################




