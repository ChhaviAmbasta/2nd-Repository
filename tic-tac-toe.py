def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(spot in ['X', 'O'] for spot in board)

def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a position (1-9): ")
        
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] not in ['X', 'O']:
                board[move] = current_player

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break

                if check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break

                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Position already taken. Choose another.")
        else:
            print("Invalid input. Choose a position (1-9).")

if __name__ == "__main__":
    tic_tac_toe()
