n, l = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
stack, answer = [], 0
for each in p:
    if not stack:
        stack.append(each)
    elif each - stack[0] >= l:
        answer += 1
        stack = [each]

if stack:
    answer += 1

print(answer)
