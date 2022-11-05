s = list(map(int, list(input())))

stack = []
zero, one = 0, 0
for i, next_ in enumerate(s):
    if not stack:
        stack.append(next_)

    elif stack and stack[-1] != next_:
        if stack[-1] == 0:
            zero += 1
        elif stack[-1] == 1:
            one += 1
        stack.append(next_)


print(max(zero, one))
