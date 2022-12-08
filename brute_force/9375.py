from collections import defaultdict
from itertools import combinations


for _ in range(int(input())):
    n = int(input())
    db = defaultdict(int)
    for _ in range(n):
        wear, category = input().split()
        db[category] += 1

    answer = 1
    for K, V in db.items():
        answer *= (V+1)

    print(answer - 1)
