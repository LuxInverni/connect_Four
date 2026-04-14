import random
import copy
from board import *

PLAYER_PIECE = 1
AI_PIECE = 2

def get_valid_columns(board, COLUMN_COUNT):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def pick_best_move(board, COLUMN_COUNT):

    valid_cols = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

    # 1. WIN
    for col in valid_cols:
        temp = copy.deepcopy(board)
        row = get_next_open_row(temp, col)
        drop_piece(temp, row, col, AI_PIECE)
        if winning_move(temp, AI_PIECE):
            return col

    # 2. BLOCK
    for col in valid_cols:
        temp = copy.deepcopy(board)
        row = get_next_open_row(temp, col)
        drop_piece(temp, row, col, PLAYER_PIECE)
        if winning_move(temp, PLAYER_PIECE):
            return col

    # 3. CENTER
    center = COLUMN_COUNT // 2
    if center in valid_cols:
        return center

    # 4. RANDOM
    return random.choice(valid_cols)

def score_center(board):
    center_col = len(board[0]) // 2
    center_count = 0

    for r in range(len(board)):
        if board[r][center_col] == AI_PIECE:
            center_count += 1

    return center_count * 3

