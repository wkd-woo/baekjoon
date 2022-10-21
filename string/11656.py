s = str(input())
answer = []
for _ in s:
    answer.append(s)
    s = s[1:]

answer.sort()
for ans in answer:
    print(ans)
