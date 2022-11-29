from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())

numDB = defaultdict(str)
nameDB = defaultdict(int)
for i in range(1, n+1):
    name = input().rstrip()
    numDB[i] = name
    nameDB[name] = i

for _ in range(m):
    ins = input().rstrip()
    if ins.isdigit():
        print(numDB[int(ins)])
    else:
        print(nameDB[ins])
