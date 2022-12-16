from sys import stdin

input = stdin.readline


n = int(input())
l = list(int(input()) for _ in range(n))
stack, answer = [], 0
for height in l:
    man = [height, 1]  # [키, 같은 키 count]
    while stack and stack[-1][0] <= height:  # 뒤에 키가 더 작은사람이 있다면
        pop = stack.pop()
        answer += pop[1]
        if pop[0] == height:  # 지나오면서 키가 같았던 사람 count
            man[1] += pop[1]

    if stack:  # 나보다 키가 더 큰사람을 만난 경우 stack이 남음
        answer += 1  # 나와 그 사람까진 볼 수 있음

    stack.append(man)  # 마지막으로 자기 자신 push

print(answer)
