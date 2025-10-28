puzzle = [[1, 2, 3],
          [4, 0, 6],
          [7, 5, 8]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]
def display(p):
    for row in p:
        for val in row:
            print(val if val != 0 else "_", end=" ")
        print()
    print()
def find_blank(p):
    for i in range(3):
        for j in range(3):
            if p[i][j] == 0:
                return i, j
def move(p, direction):
    x, y = find_blank(p)
    if direction == "up" and x > 0:
        p[x][y], p[x-1][y] = p[x-1][y], p[x][y]
    elif direction == "down" and x < 2:
        p[x][y], p[x+1][y] = p[x+1][y], p[x][y]
    elif direction == "left" and y > 0:
        p[x][y], p[x][y-1] = p[x][y-1], p[x][y]
    elif direction == "right" and y < 2:
        p[x][y], p[x][y+1] = p[x][y+1], p[x][y]
    else:
        print("Invalid move!")
    return p
print("Initial Puzzle:")
display(puzzle)
while puzzle != goal:
    move_dir = input("Enter move (up/down/left/right): ").lower()
    puzzle = move(puzzle, move_dir)
    display(puzzle)
    if puzzle == goal:
        print(" Congratulations! You solved the puzzle!")
        break

