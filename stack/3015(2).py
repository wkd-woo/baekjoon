from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
stack = []
NGE = [0 for i in range(len(l))]
mx = -int(1e9)
db = []
for each in l:
    mx = max(mx, each)
    db.append(mx)

for i in range(n):
    x = l[i]  # 하나씩 수 확인
    mx = db[i]
    if not stack or stack[-1][0] >= mx:
        stack.append((mx, x, i))  # (수, 인덱스) 형태로 삽입
    else:
        while stack:
            mx, previous, index = stack.pop()  # 역방향으로 하나씩 꺼내기
            if previous >= mx:  # 이전 수가 현재 수보다 크다면
                stack.append((previous, previous, index))  # 다시 스택에 넣음
                break
            else:
                # 이전 수가 현재 수보다 작으면 기록
                NGE[index] = i - index
        stack.append((mx, x, i))  # (수, 인덱스) 형태로 삽입

answer = 0  # 기본적으로 바로 앞에 있는 사람은 볼 수 있음
for res in NGE:
    answer += res

print(NGE)
print(answer)
