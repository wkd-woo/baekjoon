import sys
import heapq

input = sys.stdin.readline

n = int(input())
left, right = list(), list()
for i in range(n):
    next_ = int(input())
    if i == 0:
        mid = next_
        answer = [mid]
        left = [(-mid, mid)]
        continue

    if next_ > mid:
        heapq.heappush(right, next_)
    else:
        heapq.heappush(left, (-next_, next_))

    while not (len(left) >= len(right)):
        temp = heapq.heappop(right)
        heapq.heappush(left, (-temp, temp))

    if len(left) > len(right) + 1:
        temp = heapq.heappop(left)[1]
        heapq.heappush(right, temp)

    mid = heapq.heappop(left)[1]
    heapq.heappush(left, (-mid, mid))
    answer.append(mid)

for each in answer:
    print(each)
