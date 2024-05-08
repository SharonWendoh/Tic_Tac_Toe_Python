import random

board = ["", "", "", "", "", "", "", "", ""]
single_player_mode = False
is_game_over = False
player_1 = ""
player_2 = ""

def restart():
    global is_game_over
    global board
    is_game_over = False
    board = ["", "", "", "", "", "", "", "", ""]

def update_player_mode(single_player: bool):
    restart()
    single_player = single_player_mode

def is_board_full(board: list) -> bool:
    for i in board:
        if i != player_1 and i != player_2:
            return False
        else:
            return True
        
def choose_random_move(board: list, moves: list) -> int:
    possible_moves = []

    for i in moves:
        if board[i] == "":
            possible_moves.append(i)

    if not possible_moves:
        return -1
    else:
        index = random.randint(0, len(possible_moves) - 1)
        return possible_moves[index]
    
