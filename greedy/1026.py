from collections import deque

N = int(input())
A = sorted(map(int, input().split()))
B = list(map(int, input().split()))
A = deque(A)
B = deque(B)
s = 0
while B:
    temp = B[0]
    if temp == max(B):
        a = A.popleft()
        b = B.popleft()
        s += a * b
    else:
        B.append(B.popleft())

print(s)