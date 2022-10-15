import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
heap = []
while a:
    heapq.heappush(heap, a.pop())

for _ in range(m):
    if len(heap) == 1:
        break
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    heapq.heappush(heap, one + two)
    heapq.heappush(heap, one + two)

print(sum(heap))
