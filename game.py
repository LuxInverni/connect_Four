import pygame
import sys
import math
import time

from constants import *
from board import *
from ui import draw_board, draw_menu
from ai import pick_best_move

game_state = "MENU"
game_mode = None  # "PVP" or "AI"
winner_text = ""

board = create_board()
print_board(board)
game_over = False
turn = 0

ai_pending = False
ai_delay_timer = 0

pygame.init()

width = 700
height = 700
size = (width, height)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

SQUARESIZE = min(
    width // COLUMN_COUNT,
    (height - 100) // ROW_COUNT  # leave space for UI
)

RADIUS = int(SQUARESIZE / 2 - 5)
pygame.display.update()

myfont = pygame.font.SysFont(
    "monospace",
    int(height * 0.06)   # ~6% of screen height
)

mouse_x = 0

while True:

    width, height = screen.get_size()

    UI_HEIGHT = int(height * 0.15)
    BOARD_HEIGHT = height - UI_HEIGHT

    SQUARESIZE = min(
        width // COLUMN_COUNT,
        BOARD_HEIGHT // ROW_COUNT
    )

    board_width = COLUMN_COUNT * SQUARESIZE
    board_height = ROW_COUNT * SQUARESIZE

    offset_x = (width - board_width) // 2
    offset_y = UI_HEIGHT

    screen.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "MENU":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    game_mode = "PVP"
                    board = create_board()
                    turn = 0
                    game_state = "PLAYING"

                elif event.key == pygame.K_a:
                    game_mode = "AI"
                    board = create_board()
                    turn = 0
                    game_state = "PLAYING"

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        elif game_state == "GAME_OVER":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = "MENU"

        elif game_state == "PLAYING":

            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]

            if event.type == pygame.MOUSEBUTTONDOWN:

                posx = event.pos[0]

                # Ignore clicks outside board
                if not (offset_x <= posx < offset_x + board_width):
                    continue

                col = (posx - offset_x) // SQUARESIZE

                # Extra safety
                if col < 0 or col >= COLUMN_COUNT:
                    continue

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, turn + 1)

                if game_mode == "AI":
                    ai_pending = True
                    ai_delay_timer = pygame.time.get_ticks()

                if winning_move(board, turn + 1):
                    winner_text = f"Player {turn + 1} wins!"
                    game_state = "GAME_OVER"

                # Only switch turn in PVP
                if game_mode == "PVP":
                    turn = (turn + 1) % 2


    # 🔥 THIS IS THE KEY FIX (frame render loop)
    if game_state == "MENU":
        draw_menu(screen, myfont)


    elif game_state == "PLAYING":

        # --- DRAW HOVER (FIRST) ---

        color = RED if turn == 0 else YELLOW

        # Clamp mouse to board

        if mouse_x < offset_x:
            mouse_x_clamped = offset_x
        elif mouse_x >= offset_x + board_width:
            mouse_x_clamped = offset_x + board_width - 1
        else:
            mouse_x_clamped = mouse_x
        col = (mouse_x_clamped - offset_x) // SQUARESIZE
        hover_x = offset_x + col * SQUARESIZE + SQUARESIZE // 2
        hover_y = UI_HEIGHT // 2
        pygame.draw.circle(screen, color, (hover_x, hover_y), RADIUS)


        # AI

        if game_mode == "AI" and ai_pending:

            if pygame.time.get_ticks() - ai_delay_timer > 400:

                ai_col = pick_best_move(board, COLUMN_COUNT)

                if ai_col is not None and is_valid_location(board, ai_col):
                    ai_row = get_next_open_row(board, ai_col)
                    drop_piece(board, ai_row, ai_col, 2)

                    if winning_move(board, 2):
                        winner_text = "AI wins!"
                        game_state = "GAME_OVER"

                ai_pending = False
                turn = 0  # return control to player

        # --- DRAW BOARD ---

        draw_board(screen, board, SQUARESIZE, RADIUS, offset_x, offset_y)
        pygame.display.update()


    elif game_state == "GAME_OVER":

        screen.fill(BLACK)
        label = myfont.render(winner_text, True, RED)
        restart = myfont.render("Press R to Restart", True, YELLOW)
        screen.blit(label, (screen.get_width() // 2 - 150, 200))
        screen.blit(restart, (screen.get_width() // 2 - 180, 300))

        pygame.display.update()