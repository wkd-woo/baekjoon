from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    line = list(input().split())
    if line[0] == 'push':
        queue.append(line[1])
    elif line[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
