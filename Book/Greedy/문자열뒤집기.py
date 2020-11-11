inputString = input()

zeroGroup, oneGroup = 0, 0

for i in range(len(inputString)-1):
    if inputString[i] == '0' and inputString[i+1] == '1':
        zeroGroup += 1
    elif inputString[i] == '1' and inputString[i+1] == '0':
        oneGroup += 1

if inputString[-1] == '0':
    zeroGroup += 1
else:
    oneGroup += 1

print(min(oneGroup, zeroGroup))