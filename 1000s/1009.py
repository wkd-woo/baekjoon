T = int(input())

for i in range(T):
    A, B = list(map(int, input().split()))
    if 1 <= A < 100 and 1 <= B < 1000000:
        A_list = list(map(int, str(A)))
        B_list = list(map(int, str(B)))
        data = (A_list.pop()) ** (B_list.pop())
        computer = data % 10 + 1
        print(computer)
