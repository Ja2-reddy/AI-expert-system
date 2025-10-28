N = 8
board = [[0] * N for _ in range(N)]

# Function to check if placing a queen is safe
def safe(row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the puzzle
def solve(row):
    if row == N:
        for r in board:
            print(r)
        print()
        return True

    for col in range(N):
        if safe(row, col):
            board[row][col] = 1
            solve(row + 1)
            board[row][col] = 0  # backtrack

# Call the function
print("Solutions for 8 Queens Problem:\n")
solve(0)

