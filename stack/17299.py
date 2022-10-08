from collections import defaultdict


n = int(input())
l = list(map(int, input().split()))
stack = []
NGE = [-1] * n
db = defaultdict(int)

for each in l:
    db[each] += 1

for i in range(n):
    x = l[i]  # 하나씩 수 확인
    freq = db[x]
    if not stack or stack[-1][0] >= freq:
        stack.append((freq, x, i))  # (빈도, 수, 인덱스) 형태로 삽입
    else:
        while stack:
            frequency, previous, index = stack.pop()  # 역방향으로 하나씩 꺼내기
            if frequency >= freq:
                stack.append((frequency, previous, index))  # 다시 스택에 넣음
                break
            else:
                NGE[index] = x  # 오등큰수 기록
        stack.append((freq, x, i))

print(*NGE)
