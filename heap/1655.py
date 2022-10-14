import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
answer = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

    temp = []
    if len(heap) % 2 == 1:  # 홀수일 때
        for _ in range(len(heap)//2+1):
            temp.append(heapq.heappop(heap))
    else:
        for _ in range(len(heap)//2):
            temp.append(heapq.heappop(heap))
    answer.append(temp[-1])
    heap.extend(temp)
    heapq.heapify(heap)

for each in answer:
    print(each)
