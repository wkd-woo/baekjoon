n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
answer = 0
while len(l) > 1:
    if max(l) <= 0:
        l.sort(reverse=True)
    one = l.pop()
    two = l.pop()

    if one * two == 0 and min(one, two) == 0:
        answer += max(one, two)
        if l:
            l.append(min(one, two))
    elif one * two == 0 and min(one, two) < 0:
        pass
    elif one * two > 0 and min(one, two) > 0:
        answer += max(one + two, one * two)
    elif one * two > 0 and min(one, two) < 0:
        answer += max(one + two, one * two)
    elif one * two < 0:
        answer += max(one, two)
        l.append(min(one, two))
    else:
        answer += max(one + two, one * two)

    l.sort()

if l:
    answer += l.pop()

print(answer)
