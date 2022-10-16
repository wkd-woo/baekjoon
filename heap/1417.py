import heapq

n = int(input())

one = int(input())
heap = []
for i in range(n-1):
    heapq.heappush(heap, (-int(input()), i))

cnt = 0
while len(heap):
    mx, i = heapq.heappop(heap)
    if -mx < one:
        break
    mx += 1
    cnt += 1
    one += 1
    heapq.heappush(heap, (mx, i))

print(cnt)
