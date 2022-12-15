n = int(input())
l = list(map(int, input().split()))
stack = []
NGE = [-1] * n

for i in range(n):
    x = l[i]  # 하나씩 수 확인
    if not stack or stack[-1][0] >= x:
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입
    else:
        while stack:
            previous, index = stack.pop()  # 역방향으로 하나씩 꺼내기
            if previous >= x:  # 이전 수가 현재 수보다 크다면
                stack.append((previous, index))  # 다시 스택에 넣음
                break
            else:
                NGE[index] = x  # 이전 수가 현재 수보다 작으면 오큰수 기록
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입

for x in NGE:  # 오큰수를 하나씩 출력
    print(x, end=' ')
