from sys import stdin
import heapq

input = stdin.readline

n = int(input())
heap = []
for _ in range(n):  # O(n)
    num, start, end = map(int, input().split())
    heapq.heappush(heap, (start, end))  # * O(log(n))

l = []
mn, mn_idx = int(1e9), 100001
while heap:  # O(n)
    temp = heapq.heappop(heap)  # * O(log(n))
    if not l:
        heapq.heappush(l, (temp[1], temp[0]))
    else:
        top = heapq.heappop(l)  # log(s)
        if top[0] > temp[0]:
            heapq.heappush(l, top)  # log(s)
        heapq.heappush(l, (temp[1], temp[0]))  # log(s)

print(len(l))
