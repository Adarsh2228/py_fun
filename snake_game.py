import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake properties
snake_size = 20
snake_speed = 10

# Create the snake
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, pygame.Rect(x[0], x[1], snake_size, snake_size))

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Change in position of the snake
    x1_change = 0
    y1_change = 0

    # Create the snake list
    snake_list = []
    snake_length = 1

    # Generate random position for the food
    food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Game loop
    while not game_over:

        # Game over screen
        while game_close:
            window.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            window.blit(message, [window_width / 2 - 300, window_height / 2 - 50])
            pygame.display.update()

            # Handle events in the game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle events in the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Check if the snake hits the boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Draw the snake and the food
        window.fill(black)
        pygame.draw.rect(window, blue, pygame.Rect(food_x, food_y, snake_size, snake_size))
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        # Set the game speed
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()

# Start the game loop
game_loop()
