from sys import stdin

input = stdin.readline


n = int(input())
l = [int(input()) for _ in range(n)]
l.reverse()

stack = []
answer = [1] * n
answer[0] = 0
for i in range(n):
    x = l[i]
    cnd = False
    if not stack or stack[-1][0] >= x:
        stack.append((x, i))

    else:
        while stack:
            previous, index = stack.pop()
            if previous > x:
                stack.append((previous, index))
                break
            elif previous == x:
                if cnd:
                    stack.append((previous, index))
                    answer[i] -= 1
                    break
                answer[i] += 1
                cnd = True
            else:
                answer[i] += 1
        stack.append((x, i))

answer.reverse()
if max(l) == l[0] or max(l) == l[-1]:
    print(sum(answer) - 1)

else:
    print(sum(answer) - 1)
