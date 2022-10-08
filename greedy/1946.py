from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    l.sort(key=lambda x: x[0])
    cnt = n
    mn = int(1e9)
    for x, y in l:
        if  mn < y:
            cnt -= 1
        mn = min(mn, y)

    print(cnt)
