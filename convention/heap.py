from sys import stdin
import heapq

input = stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if not x and heap:
        print(heapq.heappop(heap)[1])
    elif not x and not heap:
        print(0)
    elif x:
        heapq.heappush(heap, (abs(x), x))