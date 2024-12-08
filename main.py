#Frogger game - as the video game with control by arrows for front, side to side and back
#befor you use it you have to install pygame - query: pip3 install pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frogger")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Frog properties
frog_x = screen_width // 2
frog_y = screen_height - 50
frog_size = 20
frog_speed = 20

# Car properties
car_width = 40
car_height = 20
cars = []
num_cars = 5
car_speed = 3

#Generate initial cars at random positions and directions
for i in range(num_cars):
    car_x = random.randint(0, screen_width - car_width)
    car_y = random.randint(50, screen_height //2 -car_height)
    car_direction = random.choice([-1, 1]) # -1 for left, 1 for right
    cars.append([car_x, car_y, car_direction])


# Game loop
running = True
score = 0
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Frog movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and frog_x > 0:
        frog_x -= frog_speed
    if keys[pygame.K_RIGHT] and frog_x < screen_width - frog_size:
        frog_x += frog_speed
    if keys[pygame.K_UP] and frog_y > 0:
        frog_y -= frog_speed
    if keys[pygame.K_DOWN] and frog_y < screen_height - frog_size:
        frog_y += frog_speed


    # Car movement and collision detection
    for i, car in enumerate(cars):
        car[0] += car[2] * car_speed
        if car[0] < 0 or car[0] > screen_width - car_width:
            car[2] *= -1  # Reverse direction

        #Collision Detection (simple bounding box)
        if (frog_x < car[0] + car_width and
            frog_x + frog_size > car[0] and
            frog_y < car[0] + car_height and
            frog_y + frog_size > car[y]):
            running = False #Game Over on collision


    #Check if frog reaches the top
    if frog_y < 50:
        score += 1
        frog_x = screen_width // 2
        frog_y = screen_height - 50


    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, green, (frog_x, frog_y, frog_size, frog_size)) # Frog

    for car in cars:
        pygame.draw.rect(screen, red, (car[0], car[1], car_width, car_height)) # Cars


    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
