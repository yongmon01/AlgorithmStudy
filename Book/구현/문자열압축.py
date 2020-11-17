input_string = input()
n = len(input_string)
min_length = n

for i in range(2, n//2+1):
    if n % i != 0:
        continue
    new_string = ""
    prev = input_string[0:i]
    repeat = 1
    for j in range(i, n, i):
        current = input_string[j:j+i]
        if current == prev:
            repeat += 1
        else:
            new_string = str(repeat) + prev
            new_string += current
            prev = current
    print(new_string)

# for i in range(1, n//2+1):
#     if n % i != 0:
#         continue
#     dictionary = {}
#     for j in range(0, n, i):
#         current = input_string[j:j+i]
#         if current not in dictionary:
#             dictionary[current] = 1
#         else:
#             dictionary[current] += 1
#     current_length = 0
#     for i in list(dictionary.items()):
#         current_length = current_length + len(i[0])
#         if i[1] != 1:
#             current_length = current_length + len(str(i[1]))
#     min_length = min(min_length, current_length)
#
# print(min_length)

