from sys import stdin
from collections import defaultdict, deque
import heapq

input = stdin.readline

n = int(input())
heap = []
for _ in range(n):  # O(n)
    d, w = map(int, input().split())
    heapq.heappush(heap, (d, -w))

# 가장 작은 것 초기화
schedule = [(0, 0)]
while heap:
    day, w = heapq.heappop(heap)
    if len(schedule) >= day:
        temp = heapq.heappop(schedule)
        if temp[0] < -w and day >= temp[1]:
            heapq.heappush(schedule, (-w, day))
        else:
            heapq.heappush(schedule, temp)
    else:
        heapq.heappush(schedule, (-w, day))

result = 0
for w, day in schedule:
    result += w

print(result)
