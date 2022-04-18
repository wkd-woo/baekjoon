from itertools import permutations

n = int(input())
numbs = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

mx = -int(1e9)
mn = int(1e9)

opers = []
for i in range(plus):
    opers.append('+')
for i in range(minus):
    opers.append('-')
for i in range(multiply):
    opers.append('*')
for i in range(divide):
    opers.append('/')

for i in permutations(opers, n - 1):
    temp = numbs[0]
    for idx, j in enumerate(i):
        if j == '+':
            temp = int(temp + numbs[idx + 1])
        elif j == '-':
            temp = int(temp - numbs[idx + 1])
        elif j == '*':
            temp = int(temp * numbs[idx + 1])
        elif j == '/':
            temp = int(temp / numbs[idx + 1])
    mx = max(mx, temp)
    mn = min(mn, temp)

print(mx)
print(mn)
