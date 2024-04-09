import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10 + depth
    elif check_winner(board, 'O'):
        return 10 - depth
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2) for player X: "))
            col = int(input("Enter column (0, 1, 2) for player X: "))
            if board[row][col] == " ":
                return row, col
            else:
                print("That spot is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Player X move
        row, col = player_move(board)
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("Player X wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        # AI move
        row, col = ai_move(board)
        board[row][col] = 'O'
        print("AI chooses row {}, column {}.".format(row, col))
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()