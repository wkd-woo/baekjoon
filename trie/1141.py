N = int(input())
l = [input() for _ in range(N)]
l.sort(key=lambda x: len(x))

answer = 0
for i in range(N):
    flag = False
    for j in range(i+1, N):
        if l[i] == l[j][0:len(l[i])]:
            flag = True
            break

    if not flag:
        answer += 1

print(answer)
