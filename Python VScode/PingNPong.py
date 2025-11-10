import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping N' Pong Game")
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 5

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.speed_x = 4
        self.speed_y = 4

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

        if self.rect.colliderect(left_paddle.rect):
            self.speed_x = -self.speed_x

        if self.rect.colliderect(right_paddle.rect):
            self.speed_x = -self.speed_x

        if self.rect.left <= 0:
            self.reset()
            return "right"
        
        if self.rect.right >= WIDTH:
            self.reset()
            return "left"
        return None
    
    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = -self.speed_x

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

left_paddle = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    left_paddle.move(pygame.K_w, pygame.K_s)
    right_paddle.move(pygame.K_UP, pygame.K_DOWN)

    scorer = ball.move()

    if scorer == "left":
        right_score += 1
    elif scorer == "right":
        left_score += 1

    if left_score >= 5:
        print("Pemain Kiri Menang!")
        running = False
    elif right_score >= 5:
        print("Pemain Kanan Menang!")
        running = False

    left_paddle.draw()
    right_paddle.draw()
    ball.draw()

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (3 * WIDTH // 4, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()