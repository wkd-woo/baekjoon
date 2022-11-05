import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    left, right = list(), list()
    l = []
    if n % 10 == 0:
        for _ in range(n//10):
            l.extend(list(map(int, input().split())))
    else:
        for _ in range(n//10+1):
            l.extend(list(map(int, input().split())))

    mid = l[0]
    result = [mid]
    for i, next_ in enumerate(l[1:], 1):
        if next_ > mid:
            heapq.heappush(right, next_)
        else:
            heapq.heappush(left, -next_)

        if i % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            result.append(mid)

    print(len(result))
    for i in range(len(result)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()
