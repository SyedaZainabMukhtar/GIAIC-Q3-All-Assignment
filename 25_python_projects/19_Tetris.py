# Requires 'pygame': pip install pygame
import asyncio
import pygame
import random
import platform

FPS = 30
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1], [1, 1]], # O
    [[1, 1, 1], [0, 1, 0]], # T
    [[1, 1, 1], [1, 0, 0]], # L
]

def create_board():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def check_collision(board, piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j]:
                if x + j < 0 or x + j >= GRID_WIDTH or y + i >= GRID_HEIGHT or (y + i >= 0 and board[y + i][x + j]):
                    return True
    return False

def merge_piece(board, piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j]:
                board[y + i][x + j] = 1

def clear_lines(board):
    lines_cleared = 0
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = GRID_HEIGHT - len(new_board)
    for _ in range(lines_cleared):
        new_board.insert(0, [0 for _ in range(GRID_WIDTH)])
    return new_board, lines_cleared

def setup():
    global screen, board, current_piece, piece_x, piece_y, clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    board = create_board()
    current_piece = random.choice(SHAPES)
    piece_x = GRID_WIDTH // 2 - len(current_piece[0]) // 2
    piece_y = 0
    clock = pygame.time.Clock()

def update_loop():
    global piece_y, current_piece, piece_x, board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not check_collision(board, current_piece, piece_x - 1, piece_y):
                piece_x -= 1
            elif event.key == pygame.K_RIGHT and not check_collision(board, current_piece, piece_x + 1, piece_y):
                piece_x += 1
            elif event.key == pygame.K_DOWN:
                piece_y += 1
    
    if not check_collision(board, current_piece, piece_x, piece_y + 1):
        piece_y += 1
    else:
        merge_piece(board, current_piece, piece_x, piece_y)
        board, _ = clear_lines(board)
        current_piece = random.choice(SHAPES)
        piece_x = GRID_WIDTH // 2 - len(current_piece[0]) // 2
        piece_y = 0
        if check_collision(board, current_piece, piece_x, piece_y):
            print("Game Over!")
            pygame.quit()
            return
    
    screen.fill(BLACK)
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if board[i][j]:
                pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    for i in range(len(current_piece)):
        for j in range(len(current_piece[0])):
            if current_piece[i][j]:
                pygame.draw.rect(screen, WHITE, ((piece_x + j) * GRID_SIZE, (piece_y + i) * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.flip()
    clock.tick(FPS)

async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())