numString = int(input())
numString = str(numString)

answer = int(numString[0])
numString = numString[1:]

for i in numString:
    i = int(i)
    if i == 0 or i == 1:
        answer += i
    else:
        answer *= i
print(answer)