import sys

n = int(input())
l = sorted(map(int, input().split()))
start, end = 0, n - 1
mix = sys.maxsize
answerL = 0
answerR = 0
while start < end:
    temp = l[start] + l[end]
    if mix == 0:
        break

    if abs(temp) < mix:
        mix = abs(temp)
        answerL = start
        answerR = end

    if temp < 0:
        start += 1
    elif temp > 0:
        end -= 1
    else:
        break

print(l[answerL], l[answerR])
