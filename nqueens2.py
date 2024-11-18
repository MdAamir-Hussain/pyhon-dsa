def print_board(board):
    """Utility function to print the board."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True


def solve_n_queens(board, row, n, solutions):
    """Recursive backtracking function to solve the N-Queens problem."""
    if row == n:
        # All queens are placed, save the board configuration
        solution = ["".join("Q" if col else "." for col in r) for r in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = True

            # Recur to place the rest of the queens
            solve_n_queens(board, row + 1, n, solutions)

            # Backtrack and remove the queen
            board[row][col] = False


def n_queens_all_solutions(n):
    """Wrapper function to solve the N-Queens problem and print all solutions."""
    board = [[False] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
    for index, solution in enumerate(solutions):
        print(f"Solution {index + 1}:")
        for row in solution:
            print(row)
        print("\n")


# Solve the 8-Queens problem and print all solutions
n_queens_all_solutions(10)
