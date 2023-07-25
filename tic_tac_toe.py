def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    while not is_board_full(board):
        current_player = players[player_index]
        print_board(board)
        move = get_move(current_player)
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            player_index = (player_index + 1) % 2
        else:
            print("That cell is already occupied. Try again.")

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
