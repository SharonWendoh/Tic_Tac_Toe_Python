#python -m pytest
import logic
from logic import restart, is_game_over, board


def test_restart():

    #print(f"Before restart: is_game_over = {is_game_over}, board = {board}")
    logic.is_game_over = True

    restart()

    #print(f"After restart: is_game_over = {is_game_over}, board = {board}")

    assert is_game_over == False
    assert board == ["", "", "", "", "", "", "", "", ""]