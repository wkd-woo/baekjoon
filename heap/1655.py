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

    # 좌/우 리스트 길이를 1 차이로 유지해야함
    # 방금 들어온 값을 좌측 최대, 우측 최소랑 비교해야함
    while len(left) <= len(right):
        temp = heapq.heappop(right)
        heapq.heappush(left, (-temp, temp))

    mid = heapq.heappop(left)[1]
    heapq.heappush(left, (-mid, mid))
    answer.append(mid)

for each in answer:
    print(each)
