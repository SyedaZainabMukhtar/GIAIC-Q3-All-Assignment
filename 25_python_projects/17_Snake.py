# Requires 'pygame': pip install pygame
import asyncio
import pygame
import random
import platform

FPS = 15
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def setup():
    global screen, snake, direction, food, clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    snake = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
    direction = (1, 0)
    food = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
    clock = pygame.time.Clock()

def update_loop():
    global snake, direction, food
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
    
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT or head in snake:
        pygame.quit()
        print("Game Over!")
        return
    
    snake.insert(0, head)
    
    if head == food:
        food = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
    else:
        snake.pop()
    
    screen.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
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