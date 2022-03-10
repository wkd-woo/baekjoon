from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
target = deque(map(int, input().split()))
cnt = 0

while target:
    if target[0] == queue[0]:  # 1번연산
        target.popleft()
        queue.popleft()
    elif queue.index(target[0]) <= len(queue) // 2:
        queue.append(queue.popleft()) # 2번연산
        cnt += 1
    elif queue.index(target[0]) > len(queue) // 2:
        queue.appendleft(queue.pop()) # 3번연산
        cnt += 1

print(cnt)