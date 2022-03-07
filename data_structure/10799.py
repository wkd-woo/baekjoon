from collections import deque

line = deque(input())
stack = []
pieces = 0
before = ''

while line:
    temp = line.popleft()
    if temp == '(':
        stack.append(temp)
    elif temp == ')' and stack:
        stack.pop()
        if before == '(' and stack:
            pieces += len(stack)
        if before == ')':
            pieces += 1

    before = temp

print(pieces)