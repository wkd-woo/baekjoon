def solution(n):
    global cnt
    if n >= 10:
        cnt += 1
        return solution(sum(list(map(int, list(str(n))))))

    if n % 3 == 0:
        return True
    else:
        return False


x = list(map(int, input()))
cnt = 1
temp = sum(x)

result = solution(temp)

if len(x) < 2:
    print(0)
    print('YES' if not x[0] % 3 else 'NO')
else:
    print(cnt)
    print('YES' if result else 'NO')
