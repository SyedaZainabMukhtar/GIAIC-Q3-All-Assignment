import random

def create_board(size, mines):
    board = [[" " for _ in range(size)] for _ in range(size)]
    mine_locations = random.sample([(i, j) for i in range(size) for j in range(size)], mines)
    
    for x, y in mine_locations:
        board[x][y] = "*"
    
    return board, mine_locations

def count_adjacent_mines(board, x, y, size):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < size and 0 <= y + j < size and board[x + i][y + j] == "*":
                count += 1
    return count

def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board)):
            if revealed[i][j]:
                if board[i][j] == "*":
                    print("*", end=" ")
                else:
                    print(count_adjacent_mines(board, i, j, len(board)), end=" ")
            else:
                print(".", end=" ")
        print()

def minesweeper():
    size = 5
    mines = 5
    board, mine_locations = create_board(size, mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    
    while True:
        print_board(board, revealed)
        x = int(input("Enter row (0-4): "))
        y = int(input("Enter column (0-4): "))
        
        if (x, y) in mine_locations:
            print("Game Over! You hit a mine!")
            revealed = [[True for _ in range(size)] for _ in range(size)]
            print_board(board, revealed)
            break
        
        revealed[x][y] = True
        if sum(row.count(True) for row in revealed) == size * size - mines:
            print("You win! All safe cells revealed!")
            print_board(board, revealed)
            break

if __name__ == "__main__":
    minesweeper()