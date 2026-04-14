import pygame
from constants import BLUE, BLACK, RED, YELLOW, ROW_COUNT, COLUMN_COUNT



def draw_menu(screen, font):
    screen.fill((0, 0, 0))

    w, h = screen.get_size()

    def draw(text, y_ratio):
        surf = font.render(text, True, (255, 255, 255))
        rect = surf.get_rect(center=(w // 2, int(h * y_ratio)))
        screen.blit(surf, rect)

    draw("CONNECT 4", 0.2)
    draw("Press P - 2 Player", 0.45)
    draw("Press A - Player vs AI", 0.55)
    draw("Press Q - Quit", 0.65)

    pygame.display.update()

def draw_board(screen, board, SQUARESIZE, RADIUS, offset_x, offset_y):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):

            # grid
            pygame.draw.rect(
                screen,
                BLUE,
                (offset_x + c * SQUARESIZE,
                 offset_y + r * SQUARESIZE,
                 SQUARESIZE,
                 SQUARESIZE)
            )

            # empty holes
            pygame.draw.circle(
                screen,
                BLACK,
                (offset_x + c * SQUARESIZE + SQUARESIZE // 2,
                 offset_y + r * SQUARESIZE + SQUARESIZE // 2),
                RADIUS
            )

    # pieces
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                color = RED
            elif board[r][c] == 2:
                color = YELLOW
            else:
                continue

            pygame.draw.circle(
                screen,
                color,
                (offset_x + c * SQUARESIZE + SQUARESIZE // 2,
                 offset_y + r * SQUARESIZE + SQUARESIZE // 2),
                RADIUS
            )

# def draw_board(screen, board, SQUARESIZE, RADIUS, offset_x, offset_y, board_height):
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT):
#             pygame.draw.rect(screen, BLUE, (offset_x + c * SQUARESIZE, offset_y + r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
#             pygame.draw.circle(
#                 screen,
#                 BLACK,
#                 (
#                     offset_x + c * SQUARESIZE + SQUARESIZE // 2,
#                     offset_y + r * SQUARESIZE + SQUARESIZE // 2
#                 ),
#                 RADIUS
#             )
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT):
#             if board[r][c] == 1:
#                 pygame.draw.circle(
#                     screen,
#                     RED,
#                     (
#                         offset_x + c * SQUARESIZE + SQUARESIZE // 2,
#                         offset_y + r * SQUARESIZE + SQUARESIZE // 2
#                     ),
#                     RADIUS
#                 )
#
#             elif board[r][c] == 2:
#                 pygame.draw.circle(
#                     screen,
#                     YELLOW,
#                     (
#                         offset_x + c * SQUARESIZE + SQUARESIZE // 2,
#                         offset_y + r * SQUARESIZE + SQUARESIZE // 2
#                     ),
#                     RADIUS
#                 )
#     pygame.display.update()

def draw_game_over(screen, font, text):
    screen.fill((0, 0, 0))

    label = font.render(text, True, (255, 255, 255))
    restart = font.render("Press R to Restart", True, (255, 255, 255))

    screen.blit(label, (100, 200))
    screen.blit(restart, (100, 300))

    pygame.display.update()