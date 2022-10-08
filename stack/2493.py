n = int(input())
l = list(map(int, input().split()))
l.reverse()

stack = []
answer = [0] * n
for i in range(n):
    x = l[i]
    if not stack or stack[-1][0] >= x:
        stack.append((x, i))
    else:
        while stack:
            previous, index = stack.pop()
            if previous >= x:
                stack.append((previous, index))
                break
            else:
                answer[index] = n - i
        stack.append((x, i))

answer.reverse()
print(*answer)
