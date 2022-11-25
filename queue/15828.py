from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
que = deque()

while True:
    ins = int(input())
    if ins == -1:
        break

    if ins == 0:
        que.popleft()
    else:
        if len(que) < n:
            que.append(ins)

print(*que)
