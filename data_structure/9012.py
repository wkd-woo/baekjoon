from collections import deque

T = int(input())


def solution(str):
    line = deque(list(str))
    height = 0

    while len(line) > 0:
        temp = line.popleft()
        if temp == '(':
            height += 1
        elif temp == ')':
            height -= 1
            if height < 0:
                return 'NO'

    if height == 0:
        return 'YES'
    else:
        return 'NO'


for _ in range(T):
    line = input()
    if 1 < len(line) <= 50:
        print(solution(line))