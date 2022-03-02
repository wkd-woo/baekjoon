from sys import stdin

n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

for l in M:
    print(1) if l in N else print(0)