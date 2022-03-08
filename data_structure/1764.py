from sys import stdin
from collections import Counter

n, m = map(int, input.split())
l = []

for _ in range(n + m):
    l.append(input)

result = []
counter = Counter(l)
for key, value in counter.items():
    if value == 2:
        result.append(key)

print(len(result))

for each in sorted(result):
    print(each)
