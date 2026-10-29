def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper-left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check the lower-left diagonal
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):
    # All queens have been placed
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main program
n = 4

board = [[0 for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print("Solution for N-Queens problem:")

    for row in board:
        print(row)
else:
    print("No solution exists.")