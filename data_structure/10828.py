from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
stack = deque()

if 1 <= N <= 10000:
    for _ in range(N):
        line = list(input().split())
        if line[0] == 'push':
            stack.append(int(line[1]))
        elif line[0] == 'pop':
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
        elif line[0] == 'top':
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)
