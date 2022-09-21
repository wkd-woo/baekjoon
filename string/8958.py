t = int(input())
for _ in range(t):
    answer, stack = 0, []
    l = list(input())

    for w in l:
        if w == 'X':
            stack.clear()
        else:
            stack.append(w)
            answer += len(stack)
    print(answer)