from collections import deque
import heapq

n = int(input())

heap = []
answer = []
for _ in range(n):
    a = input().split()
    if a[0] == '0':
        if not heap:
            answer.append(-1)
        else:
            answer.append(-heapq.heappop(heap))
    else:
        a = deque(map(int, a))
        a.popleft()
        while a:
            heapq.heappush(heap, -a.popleft())

for each in answer:
    print(each)
