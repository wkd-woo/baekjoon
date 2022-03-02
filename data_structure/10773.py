from sys import stdin

k = int(stdin.readline())
stack = []

for _ in range(k):
    insert = int(stdin.readline())
    if insert == 0 and len(stack) > 0:
        stack.pop()
    else:
        stack.append(insert)

print(sum(stack))