from sys import stdin

input = stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
stack = []
NGE = [[-1, 1] for i in range(len(l))]


for i in range(n):
    x = l[i]  # 하나씩 수 확인
    if not stack or stack[-1][0] >= x:
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입
    else:
        while stack:
            previous, index = stack.pop()  # 역방향으로 하나씩 꺼내기
            if previous < x:  # 이전 수가 현재 수보다 크다면
                stack.append((previous, index))  # 다시 스택에 넣음
                break
            else:
                # 이전 수가 현재 수보다 작으면 기록
                NGE[index] = [x, len(l[i:index])]
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입

answer = 0  # 기본적으로 바로 앞에 있는 사람은 볼 수 있음
for _, res in NGE:
    answer += res

print(NGE)
print(answer)
