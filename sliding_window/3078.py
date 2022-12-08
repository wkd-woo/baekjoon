from sys import stdin
from collections import deque, defaultdict
from bisect import bisect_left

input = stdin.readline

n, k = map(int, input().split())
l = [len(input()) for _ in range(n)]
db = defaultdict(list)

# 길이 순으로 묶음
for i, length in enumerate(l):  # O(n)
    db[length].append(i)

answer = 0
for K, V in db.items():  # O(20)
    V = deque(V)
    while V:  # O(300k * log(300k) * 20) =: O(3m)
        poll = V.popleft()  # O(n)
        idx = bisect_left(V, poll + k+1)  # 이진 탐색. O(log(n))
        answer += idx

print(answer)
