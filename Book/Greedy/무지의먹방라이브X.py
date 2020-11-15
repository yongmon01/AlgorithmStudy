# 시간초과...

# def solution(food_times, k):
#     index, count = 0, 0
#     while count < k:
#         if food_times[index % len(food_times)] == 0:
#             index += 1
#             continue
#         food_times[index % len(food_times)] -= 1
#         index += 1
#         count += 1
#     for i in range(len(food_times)):
#         if food_times[(index) % len(food_times)] != 0:
#             return (index) % len(food_times) + 1
#         index += 1
#     return -1
