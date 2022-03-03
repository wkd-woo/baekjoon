from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

stack = deque()

if 1 <= n <= 10000:
    for _ in range(n):
        line = list(input().split())
        if line[0] == 'push_front':
            stack.appendleft(int(line[1]))
        elif line[0] == 'push_back':
            stack.append(int(line[1]))
        elif line[0] == 'pop_front':
            if len(stack) > 0:
                print(stack.popleft())
            else:
                print(-1)
        elif line[0] == 'pop_back':
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        elif line[0] == 'size':
            print(len(stack))
        elif line[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif line[0] == 'back':
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)
        elif line[0] == 'front':
            if len(stack) > 0:
                print(stack[0])
            else:
                print(-1)