from sys import stdin
from collections import deque

input = stdin.readline

while True:
    cmd = list(map(int, input().split()))
    n, l = cmd[0], cmd[1:]
    if n == 0:
        break
    stack = deque()
    result = max(max(l), min(l) * len(stack))
    for each in l:
        if not stack or stack[0] <= each:
            stack.append(each)
        else:
            while stack:
                result = max(result, min(stack) * len(stack))
                stack.popleft()
    if stack:
        result = max(result, min(stack) * len(stack))

    print(result)
