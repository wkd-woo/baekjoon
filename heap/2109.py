from sys import stdin
from collections import defaultdict, deque
import heapq

input = stdin.readline

n = int(input())
heap = []
for _ in range(n):  # O(n)
    p, d = map(int, input().split())
    heapq.heappush(heap, (d, -p))

# 가장 작은 것 초기화
schedule = [(0, 0)]
while heap:
    day, pay = heapq.heappop(heap)
    if len(schedule) >= day:  # 스케쥴이 꽉 찬 경우
        temp = heapq.heappop(schedule)  # 제일 돈을 적게주는 스케쥴을 뻄
        if temp[0] < -pay and day >= temp[1]:  # 페이 비교
            heapq.heappush(schedule, (-pay, day))  # 새 스케쥴이 돈을 더 많이주면 바꿈
        else:  # 아니면 그대로
            heapq.heappush(schedule, temp)
    else:  # 스케쥴 널널하면 그냥 넣음
        heapq.heappush(schedule, (-pay, day))

result = 0
for pay, day in schedule:
    result += pay

print(result)
