word = input()
word_list = []
nums = 0
for i in word:
    if i >= 'A' and i <= 'Z':
        word_list.append(i)
    else:
        nums += int(i)

word_list.sort()
string = "".join(word_list)
if nums != 0:
    string += str(nums)
print(string)