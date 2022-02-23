t = int(input())

# 0과 1의 관계를 찾아야함
for _ in range(t):
    n = int(input())
    count_0 = [1, 0]
    count_1 = [0, 1]

    for i in range(2, n + 1):
        count_0.append(count_0[i - 1] + count_0[i - 2])  # 0 => 이전 0 두개를 더한 것
        count_1.append(count_1[i - 1] + count_1[i - 2])  # 1 => 이전 1 두개를 더한 것

    print(count_0[n], count_1[n])
