word = input()
answer_list = []

for i in range(1, len(word)//2+1):
    # if len(word) % i != 0:
    #     continue
    equal = 1
    return_string = ""
    for j in range(0,len(word)-i+1,i):
        #print(j,j+i)
        #print(j+i, j+2*i)
        if word[j: j+i] == word[j+i: j + 2*i]:
            equal += 1
        else:
            if equal == 1:
                return_string += word[j: j+i]
            else:
                return_string += str(equal) + word[j: j+i]
                equal = 1
    if len(word) % i != 0:
        return_string += word[-(len(word) % i):]
    answer_list.append(return_string)
answer_list.sort(key = lambda x: len(x))
print(answer_list)
print(len(answer_list[0]))
#abcabcabcabcdededededede
