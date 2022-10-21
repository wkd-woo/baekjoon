from itertools import permutations


n = int(input())
k = int(input())
nums = [input() for _ in range(n)]

db = set()
for each in list(permutations(nums, k)):
    db.add("".join(each))


print(len(db))
