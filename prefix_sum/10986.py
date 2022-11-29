from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
db = {i: 0 for i in range(m)}  # O(m)
db[0], total = 1, 0
for i in range(n):
    total += l[i]  # O(n) = O(1,000,000)
    db[total % m] += 1  # 누적 합의 나머지가 같은 것을 찾음

cnt = 0
for V in db.values():
    cnt += V * (V-1) // 2  # 조합

print(cnt)
