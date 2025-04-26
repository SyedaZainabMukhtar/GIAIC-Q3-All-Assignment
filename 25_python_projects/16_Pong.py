# Requires 'pygame': pip install pygame
import asyncio
import pygame
import platform

FPS = 60
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def setup():
    global screen, paddle1, paddle2, ball, ball_speed, clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    paddle1 = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
    ball_speed = [5, 5]
    clock = pygame.time.Clock()

def update_loop():
    global ball_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 5
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 5
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 5
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += 5
    
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]
    
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH//2 - BALL_SIZE//2
        ball.y = HEIGHT//2 - BALL_SIZE//2
        ball_speed[0] = -ball_speed[0]
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
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