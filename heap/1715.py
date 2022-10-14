import sys
import heapq
input = sys.stdin.readline


n = int(input())
heap = []
for _ in range(n):
    card = int(input())
    heapq.heappush(heap, card)

result = 0
while len(heap):
    if len(heap) == 1:
        break
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    result += one + two
    heapq.heappush(heap, one + two)

if n == 1:
    print(0)
else:
    print(result)
