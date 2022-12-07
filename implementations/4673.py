not_self_num = set()
for i in range(1, 10000):
    while True:
        new = i + sum(map(int, list(str(i))))
        if new > 10000:
            break
        if new in not_self_num:
            break
        not_self_num.add(new)

result = [i for i in range(1, 10001) if i not in not_self_num]
for each in result:
    print(each)
