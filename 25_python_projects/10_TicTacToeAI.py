import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe_ai():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    while True:
        print_board(board)
        row = int(input("Player X, enter row (0-2): "))
        col = int(input("Player X, enter column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = "X"
            if check_winner(board, "X"):
                print_board(board)
                print("Player X wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            print("AI is thinking...")
            ai_row, ai_col = ai_move(board)
            board[ai_row][ai_col] = "O"
            if check_winner(board, "O"):
                print_board(board)
                print("AI wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
        else:
            print("Cell already taken!")

if __name__ == "__main__":
    tic_tac_toe_ai()