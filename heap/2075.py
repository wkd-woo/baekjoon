from sys import stdin
import heapq

input = stdin.readline


n = int(input())
heap = []
for _ in range(n):
    l = list(map(int, input().split()))
    for each in l:
        heapq.heappush(heap, each)
    while len(heap) > n:
        heapq.heappop(heap)

answer = heapq.heappop(heap)
print(answer)
