n = int(input())
answer = n
for _ in range(n):
    s = list(input())
    db, stack = set(), []

    for w in s:
        if not stack:
            stack.append(w)
        elif stack[-1] == w:
            stack.append(w)
        elif w in db and stack[-1] != w:
            answer -= 1
            break
        else:
            stack.append(w)
        db.add(w)

print(answer)