n, m = map(int, input().split())

db = dict()
for _ in range(n):
    address, pwd = input().split()
    db[address] = pwd

target = [input() for _ in range(m)]
for each in target:
    print(db[each])
