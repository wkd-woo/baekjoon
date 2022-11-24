from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

answer = 0
db = {i: 1 for i in range(n)}  # 기본적으로 바로 앞은 볼 수 있음
db[n-1] = 0  # 마지막 제외
stack = deque()  # 증가 스택
last, mx, mx_idx = 0, l[0], 0  # 마지막 증가 인덱스, 그리고 지금까지 최대값, 최대값 인덱스
for i, person in enumerate(l):  # O(n)
    if person > mx:
        if i - last > 1:
            db[last] += 1
            if i - last > 2:
                db[last] += 1
        mx = person
        last = i
    else:
        if i - last > 1 and l[i] >= l[i-1]:
            db[last] += 1


while len(stack) > 1:
    next_ = stack.popleft()
    if next_[0] != 0:
        db[next_[0]] += 1


print(sum(db.values()))
print(db)
