A, B = map(int, input().split())
cnt = 1
while A < B:
    if B % 10 == 1:
        B = B // 10
    elif B % 2 == 0:
        B = B // 2
    else:
        break
    cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)