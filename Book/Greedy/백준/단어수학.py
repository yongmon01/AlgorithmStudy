# 1339번

n = int(input())
words = []
answer = 0
for i in range(n):
    words.append(input())
# print(words)
chars = []
numbers = []

for word in words:
    length = len(word) - 1
    for char in word:
        if char in chars:
            index = chars.index(char)
            numbers[index] += (10 ** length)
        else:
            chars.append(char)
            numbers.append(10 ** length)
        length -= 1
# print(chars)
# print(numbers)

answers = []
for i in range(len(chars)):
    answers.append((numbers[i], chars[i]))
answers.sort(reverse=True)
# print(answers)

for i in range(len(answers)):
    answer += (answers[i][0] * (9-i))

print(answer)
