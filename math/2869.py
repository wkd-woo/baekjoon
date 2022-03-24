from sys import stdin

input = stdin.readline

a, b, v = map(int, input().split())

day = a - b
cnt = (v - a) // day

if ((v - a) / day - cnt) != 0:
    cnt += 1

if 0 < cnt < 1:
    cnt = 1

print(1 + cnt)