A, B = input().split()
mn_a, mx_a = [], []
mn_b, mx_b = [], []
for a in A:
    if a == '6':
        mn_a.append('5')
    else:
        mn_a.append(a)

    if a == '5':
        mx_a.append('6')
    else:
        mx_a.append(a)

for b in B:
    if b == '6':
        mn_b.append('5')
    else:
        mn_b.append(b)

    if b == '5':
        mx_b.append('6')
    else:
        mx_b.append(b)

mn_a, mn_b = int(''.join(mn_a)), int(''.join(mn_b))
mx_a, mx_b = int(''.join(mx_a)), int(''.join(mx_b))

print(mn_a + mn_b, mx_a + mx_b)
