import pygame
import numpy as np
from Classes import NewtonsCradle, Particle

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Newton's Cradle")

# Set up the clock
clock = pygame.time.Clock()

# Create particles
Particle_1 = Particle(
    position=np.array([SCREEN_WIDTH/4, SCREEN_HEIGHT/2, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name="Particle 1",
    mass=1,
    radius=20,
    colour=BLACK
)
Particle_2 = Particle(
    position=np.array([3*SCREEN_WIDTH/4, SCREEN_HEIGHT/2, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name="Particle 2",
    mass=1,
    radius=20,
    colour=BLACK
)
pl = [Particle_1, Particle_2]

# Create the Newton's Cradle object
newtonscradle = NewtonsCradle(particles_list=pl, length=SCREEN_WIDTH/2, psi=np.pi/12)

# Set up time variables
dt = 0.01
t = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particle positions
    newtonscradle.movement()
    newtonscradle.collision_detection()
    #newtonscradle.FOTIerror()
    for j in range(newtonscradle.NUM_BALLS):
        newtonscradle.particles_list[j].Euler(dt)

    # Fill the background
    screen.fill(WHITE)

    # Draw the particles
    for particle in newtonscradle.particles_list:
        pygame.draw.circle(screen, particle.colour, (int(particle.position[0]), int(particle.position[1])), particle.radius)

    # Update the screen
    pygame.display.update()

    # Update the clock
    clock.tick(60)

pygame.quit()
