def process(n):
    li = []
    if n % 5 == 0:
        li.append(n//5)
    if n % 3 == 0:
        li.append(n//3)
    if n % 2 == 0:
        li.append(n//2)
    li.append(n-1)
    return li

x = 26
count = 0
data_list = [26]
while 1 not in data_list:
    current_list = []
    for i in data_list:
        new_list = process(i)
        current_list += new_list
    data_list = current_list
    print(data_list)
    count += 1
print(count)
