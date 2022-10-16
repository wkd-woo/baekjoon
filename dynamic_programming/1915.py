def solution(board):
    answer = 0
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 0:
            return 0
        else:
            return 1

    if sum(sum(board, [])) != 0:
        answer = 1

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j], board[i]
                                  [j-1], board[i-1][j-1]) + 1

                answer = max(answer, board[i][j])

    return answer**2


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, (list(input())))))
print(solution(matrix))
