from sys import stdin

input = stdin.readline


n = int(input())
l = list(int(input()) for _ in range(n))
stack, answer = [], 0
for height in l:
    plot = [height, 1]  # [높이,  count]
    while stack and stack[-1][0] <= height:  # 뒤에 높이가 더 낮은게 있다면
        pop = stack.pop()
        answer = max(answer, pop[0] * (pop[1] + 1))
        if pop[0] >= height:  # 지나오면서 더 높으면 기록
            plot[1] += pop[1]

    stack.append(plot)  # 마지막으로 자기 자신 push

print(answer)
