import pygame
import Classes

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Newton's Cradle")

# Create Newton's Cradle
newtons_cradle = NewtonsCradle(SCREEN_WIDTH / 2 - (NUM_BALLS - 1) * (BALL_RADIUS * 2 + CHAIN_LENGTH) / 2, 50)

# Set up game loop
running = True
clock = pygame.time.Clock()
time_step = 0.01

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                newtons_cradle.reset()
    pygame.draw.circle(screen, BALL_COLOR, (int(SCREEN_WIDTH/2), int(-SCREEN_WIDTH/2)), BALL_RADIUS)