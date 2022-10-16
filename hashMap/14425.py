from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
db = {input() for _ in range(n)}
cnt = 0
for _ in range(m):
    s = input()
    if s in db:
        cnt += 1

print(cnt)
