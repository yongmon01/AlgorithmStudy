numbers = list(map(int, input()))
print(numbers)
answer = numbers[0]
del numbers[0]

for n in numbers:
    if answer == 0 or answer == 1:
        answer += n
    elif n == 1 or n == 0:
        answer += n
    else:
        answer *= n
print(answer)