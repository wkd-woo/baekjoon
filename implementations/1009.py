T = int(input())

one = [0, 1, 5, 6]
two = [4, 9]
four = [2, 3, 7, 8]

for i in range(T):
    A, B = list(map(int, input().split()))
    if 1 <= A < 100 and 1 <= B < 1000000:

        A_list = list(map(int, str(A)))
        B_list = list(map(int, str(B)))
        A_last = A_list.pop()
        B_last = B_list.pop()

        if A_last in one:
            computer = A_last
            if computer == 0:
                computer = 10
        elif A_last in two:
            if B_last % 2 == 1:
                computer = A_last
            else:
                computer = (A_last ** 2) % 10
        elif A_last in four:
            case = B % 4
            if case == 0:
                case = 4
            computer = (A_last ** case) % 10

        print(computer)
