import re

n = int(input())
result = re.findall('\d+', input())

print(sum(list(map(int, result))))