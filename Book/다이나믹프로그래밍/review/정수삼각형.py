n = int(input())

inputs = []
for i in range(n):
    inputs.append(list(map(int, input().split())))

numbers = [[inputs[0][0]]]

for i in range(1, n):
    current_answer = []
    current = inputs[i]
    # numbers[0] += current[0]
    current_answer.append(numbers[-1][0]+ current[0])
    for j in range(1, len(numbers)):
        current_answer.append(max(numbers[-1][j-1], numbers[-1][j]) + current[j])
    # print(numbers[-1], current[-1])
    current_answer.append(numbers[-1][-1] + current[-1])
    numbers.append(current_answer)

#print(numbers)
print(max(numbers[-1]))

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5