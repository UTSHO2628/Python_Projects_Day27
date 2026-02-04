import pygame
import random
import sys

# Initialize Pygame.
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birds Flying and People Watching")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(50, HEIGHT // 2)
        self.speed = random.uniform(2, 5)

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = 0

    def draw(self):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), 5)
        pygame.draw.line(screen, BLACK, (self.x - 10, self.y - 5), (self.x, self.y), 2)  # Wing 1
        pygame.draw.line(screen, BLACK, (self.x - 10, self.y + 5), (self.x, self.y), 2)  # Wing 2

# Draw people
def draw_people():
    for i in range(10):
        x = i * 80 + 40
        pygame.draw.rect(screen, BROWN, (x, HEIGHT - 120, 20, 100))  # Body
        pygame.draw.circle(screen, BLACK, (x + 10, HEIGHT - 130), 10)  # Head

# Main loop
def main():
    birds = [Bird() for _ in range(10)]  # Create 10 birds
    running = True

    while running:
        screen.fill(BLUE)  # Sky background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move and draw birds
        for bird in birds:
            bird.move()
            bird.draw()

        # Draw people watching
        draw_people()

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
