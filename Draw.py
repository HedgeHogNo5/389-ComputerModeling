import pygame
import Classes as cl


def draw(self, surface):
    pygame.draw.circle(surface, cl.BALL_COLOR, (int(self.x), int(self.y)), cl.BALL_RADIUS)

def draw(self, surface):
    for ball in self.balls:
        ball.draw(surface)
    pygame.draw.line(surface, CHAIN_COLOR, (self.x, self.y), (self.balls[0].x, self.balls[0].y), 2)
    pygame.draw.line(surface, CHAIN_COLOR, (self.x + (NUM_BALLS - 1) * (BALL_RADIUS * 2 + CHAIN_LENGTH), self.y),
                     (self.balls[-1].x, self.balls[-1].y), 2)
    for i in range(NUM_BALLS - 1):
        start_ball = self.balls[i]
        end_ball = self.balls[i + 1]
        pygame.draw.line(surface, CHAIN_COLOR, (start_ball.x, start_ball.y), (end_ball.x, end_ball.y), 2)

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((cl.SCREEN_WIDTH, cl.SCREEN_HEIGHT))
pygame.display.set_caption("Newton's Cradle")

# Create Newton's Cradle
newtons_cradle = cl.NewtonsCradle(cl.SCREEN_WIDTH / 2 - (cl.NUM_BALLS - 1) * (cl.BALL_RADIUS * 2 + cl.CHAIN_LENGTH) / 2, 50)

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
    pygame.draw.circle(screen, cl.BALL_COLOR, (int(cl.SCREEN_WIDTH/2), int(-cl.SCREEN_WIDTH/2)), cl.BALL_RADIUS)