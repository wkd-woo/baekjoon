from string import ascii_uppercase
from collections import deque

S = list(input())
uppercases = list(ascii_uppercase)
order = {uppercase: i for i, uppercase in enumerate(uppercases)}
for i in range(1, len(S)):
    q = deque()
    S = deque(S)
    if order[S[i-1]] > order[S[i]]:
        for _ in range(i):
            q.append(S.popleft())
        while q:
            S.appendleft(q.popleft())

answer = []
temp_S = "".join(list(reversed(S)))
answer.append(temp_S)
S.appendleft(S.pop())
S = list(S)
answer.append("".join(S[::-1]))
answer.sort()
print(answer[0])
