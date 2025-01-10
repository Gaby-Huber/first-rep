import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping-Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_color = black
ball_position = [screen_width // 2, screen_height // 2]
ball_velocity = [random.choice([5, -5]), random.choice([5, -5])]

# Paddle properties
paddle_width = 150
paddle_height = 20
paddle_color = black
paddle_position = [screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10]
paddle_speed = 10

clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get key states
        keys = pygame.key.get_pressed()

        # Move paddle
        if keys[pygame.K_LEFT] and paddle_position[0] > 0:
            paddle_position[0] -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_position[0] < screen_width - paddle_width:
            paddle_position[0] += paddle_speed

        # Move ball
        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]

        # Ball collision with walls
        if ball_position[0] - ball_radius < 0 or ball_position[0] + ball_radius > screen_width:
            ball_velocity[0] *= -1
        if ball_position[1] - ball_radius < 0:
            ball_velocity[1] *= -1

        # Ball collision with paddle
        if (paddle_position[1] < ball_position[1] + ball_radius < paddle_position[1] + paddle_height and
            paddle_position[0] < ball_position[0] < paddle_position[0] + paddle_width):
            ball_velocity[1] *= -1

        # Ball out of bounds
        if ball_position[1] + ball_radius > screen_height:
            ball_position[0] = screen_width // 2
            ball_position[1] = screen_height // 2
            ball_velocity[1] *= -1

        # Clear screen
        screen.fill(white)

        # Draw paddle
        pygame.draw.rect(screen, paddle_color, (paddle_position[0], paddle_position[1], paddle_width, paddle_height))

        # Draw ball
        pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

        # Update display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
