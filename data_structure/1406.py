from sys import stdin

input = stdin.readline

stack_left = list(input().strip())
stack_right = []
n = len(stack_left)
m = int(input())

idx = n
for _ in range(m):
    temp = list(input().split())
    first = temp[0]
    second = ''

    if len(temp) == 2:
        second = temp[1]

    if first == 'P':
        stack_left.append(second)
    elif first == 'D' and stack_right:
        stack_left.append(stack_right.pop())
    elif first == 'L' and stack_left:
        stack_right.append(stack_left.pop())
    elif first == 'B' and stack_left:
        stack_left.pop()

print("".join(stack_left + reversed(stack_right)))
