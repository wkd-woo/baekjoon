n, m = map(int, input().split())

answer = 0
l = [tuple(map(int, input().split())) for _ in range(m)]
mn_pack = sorted(l, key=lambda x: (x[0]))[0][0]
mn_each = sorted(l, key=lambda x: (x[1]))[0][1]

while n > 0:
    b = min(n, 6)
    # 6개 최소비용 vs b개를 낱개최소
    answer += min(mn_each * b, mn_pack)
    n -= b

print(answer)
