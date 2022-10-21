n = int(input())

set = set()
for _ in range(n):
    name, inout = input().split()
    if inout == "enter":
        set.add(name)
    else:
        set.remove(name)


l = sorted(set, reverse=True)

for each in l:
    print(each)
