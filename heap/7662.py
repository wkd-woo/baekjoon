from sys import stdin
import heapq

input = stdin.readline


def solution(operations):
    heap = []
    mx, mn = -int(1e9), int(1e9)
    for oper in operations:
        order, num = oper
        num = int(num)
        if order == 'I':
            heapq.heappush(heap, [num, num])
        else:
            heapq.heapify(heap)
            if num == -1 and heap:
                heapq.heappop(heap)
            else:
                for i in range(len(heap)):
                    heap[i][0] = -heap[i][0]
                heapq.heapify(heap)
                if heap:
                    heapq.heappop(heap)
                for i in range(len(heap)):
                    heap[i][0] = -heap[i][0]

    if not heap:
        return "EMPTY"
    for each in heap:
        mx, mn = max(mx, each[1]), min(mn, each[1])
    return [mx, mn]


result = []
for _ in range(int(input())):
    k = int(input())
    operations = []
    for _ in range(k):
        i, n = input().split()
        operations.append([i, int(n)])

    result.append(solution(operations))

for each in result:
    if each == "EMPTY":
        print("EMPTY")
    else:
        print(*each)
