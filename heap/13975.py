import sys
import heapq
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)

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
