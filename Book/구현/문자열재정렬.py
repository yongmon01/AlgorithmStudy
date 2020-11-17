string = input()
alpha_list = []
num_sum = 0

for i in string:
    if i >= 'A' and i <= 'Z':
        alpha_list.append(i)
    else:
        num_sum += int(i)

alpha_list.sort()
alpha_list.append(str(num_sum))

print('-'.join(alpha_list))
