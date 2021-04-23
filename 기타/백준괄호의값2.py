from collections import deque

def is_okay(paren):
    q = deque()
    for i in paren:
        print(i)
        if i == '(':
            q.append(i)
        elif i == '[':
            q.append(i)
        elif i == ')':
            if not q:
                return False
            elif q.pop() != '(':
                return False
        elif i == ']':
            if not q:
                return False
            elif q.pop() != '[':
                return False
    if q:
        return False
    else:
        return True

def calculate(paren):

    q = deque()
    for i in paren:
        if i == '(':
            q.append(i)
        elif i == '[':
            q.append(i)
        elif i == ')':
            tmp = 2
            while True:
                t = q.pop()
                if type(t) == int:
                    tmp *= t
                elif t == '(':
                    q.append(tmp)
                    break
        elif i == ']':
            tmp = 3
            while True:
                t = q.pop()
                if type(t) == int:
                    tmp *= t
                elif t == '[':
                    q.append(tmp)
                    break

        sum = 0
        while q:
            node = q.pop()
            if type(node) == int:
                sum += node
            else:
                q.append(node)
                break
        if sum != 0:
            q.append(sum)

    return q[-1]
# (()[[]])([])
paren = list(input())
print(paren)
if is_okay(paren):
    print(calculate(paren))
else:
    print(0)



# from collections import deque
#
# def is_okay(paren):
#     q = deque()
#     for i in paren:
#         print(i)
#         if i == '(':
#             q.append(i)
#         elif i == '[':
#             q.append(i)
#         elif i == ')':
#             if not q:
#                 return False
#             elif q.pop() != '(':
#                 return False
#         elif i == ']':
#             if not q:
#                 return False
#             elif q.pop() != '[':
#                 return False
#     if q:
#         return False
#     else:
#         return True
#
# def calculate(paren):
#
#     q = deque()
#     for i in paren:
#         if i == '(':
#             q.append(i)
#         elif i == '[':
#             q.append(i)
#         elif i == ')':
#             num = 2
#             node = q.pop()
#             if type(node) == int:
#                 num *= node
#                 q.pop()
#                 q.append(num)
#             elif node == '(':
#                 q.append(num)
#         elif i == ']':
#             num = 3
#             node = q.pop()
#             if type(node) == int:
#                 num *= node
#                 q.pop()
#                 q.append(num)
#             elif node == '(':
#                 q.append(num)
#
#         sum = 0
#         while q:
#             node = q.pop()
#             if type(node) == int:
#                 sum += node
#             else:
#                 q.append(node)
#                 break
#         if sum != 0:
#             q.append(sum)
#
#     return q[-1]
# # (()[[]])([])
# paren = list(input())
# print(paren)
# if is_okay(paren):
#     print(calculate(paren))
# else:
#     print(0)