from sys import stdin

n = int(stdin.readline())

stack = []
result = []
target = []
output = []
now = 0
num = 1
for _ in range(n):
    target.append(int(stdin.readline()))

# result가 나올 때 까지
while len(result) < n:
    # stack이 비었거나, target보다 숫자가 작은 경우
    if len(stack) == 0 or target[now] > stack[-1]:
        stack.append(num)
        num += 1  # 숫자 1 증가시킴 push+
        output.append('+')
    elif target[now] == stack[-1]:  # stack의 끝 값이 target과 같은 경우
        result.append(stack.pop())  # 결과에 집어 넣음 pop-
        now += 1  # 다음 target으로
        output.append('-')
    elif target[now] < stack[-1]:
        break

if len(result) == n:
    for each in output:
        print(each)
else:
    print('NO')
